import Fuse from 'fuse.js'

window.addEventListener('DOMContentLoaded', async () => {
  const holder = document.getElementById('search-results')
  const input = document.getElementById('search-box')
  if (!holder || !input) return
  const query = new URLSearchParams(window.location.search).get('keyword')?.trim()

  function showMessage (message) {
    const paragraph = document.createElement('p')
    paragraph.textContent = message
    holder.append(paragraph)
  }

  if (!query) {
    showMessage(holder.dataset.empty)
    return
  }
  input.value = query

  try {
    const response = await fetch(holder.dataset.index)
    if (!response.ok) throw new Error(String(response.status))
    const pages = await response.json()
    const fuse = new Fuse(pages, {
      shouldSort: true,
      threshold: 0.1,
      minMatchCharLength: 1,
      keys: [
        { name: 'title', weight: 0.8 },
        { name: 'summary', weight: 0.6 },
        { name: 'contents', weight: 0.5 },
        { name: 'tags', weight: 0.3 },
        { name: 'categories', weight: 0.3 }
      ]
    })
    const results = fuse.search(query)
    if (!results.length) {
      showMessage(holder.dataset.noMatches)
      return
    }

    // 테마와 같은 카드 구조에 값을 텍스트로 채워 넣습니다.
    const template = document.getElementById('search-result-template').textContent
    for (const { item } of results) {
      const card = new DOMParser().parseFromString(template, 'text/html').querySelector('.post-card')
      for (const link of card.querySelectorAll('.post-card-link, .card-footer a')) link.href = item.permalink
      card.querySelector('img').src = item.hero
      card.querySelector('.card-title').textContent = item.title
      card.querySelector('.post-summary').textContent = item.summary
      card.querySelector('.card-footer span').textContent = item.date
      const tags = card.querySelector('.tags ul')
      if (tags) {
        tags.replaceChildren()
        for (const tag of item.tags || []) {
          const entry = document.createElement('li')
          entry.className = 'rounded'
          const link = document.createElement('a')
          link.className = 'btn btn-sm btn-info'
          link.textContent = tag
          link.href = holder.dataset.tagsBase + encodeURIComponent(tag.toLowerCase().replace(/\s+/g, '-')) + '/'
          entry.append(link)
          tags.append(entry)
        }
      }
      holder.append(card)
    }
  } catch {
    showMessage(holder.dataset.error)
  }
})
