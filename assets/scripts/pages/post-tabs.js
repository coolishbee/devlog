document.querySelectorAll('[data-post-tabs]').forEach(group => {
  const tabs = Array.from(group.querySelectorAll('[role="tab"]'))
  const activate = tab => {
    tabs.forEach(item => {
      const selected = item === tab
      item.setAttribute('aria-selected', String(selected))
      item.tabIndex = selected ? 0 : -1
      document.getElementById(item.getAttribute('aria-controls')).hidden = !selected
    })
    tab.focus({ preventScroll: true })
    tab.scrollIntoView({ block: 'nearest', inline: 'nearest' })
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activate(tab))
    tab.addEventListener('keydown', event => {
      let next
      switch (event.key) {
        case 'ArrowRight': next = (index + 1) % tabs.length; break
        case 'ArrowLeft': next = (index - 1 + tabs.length) % tabs.length; break
        case 'Home': next = 0; break
        case 'End': next = tabs.length - 1; break
        default: return
      }
      event.preventDefault()
      activate(tabs[next])
    })
  })
})
