const label = '코드 복사'

document.querySelectorAll('pre > code').forEach((codeBlock) => {
  const button = document.createElement('button')
  button.type = 'button'
  button.title = label
  button.setAttribute('aria-label', label)
  button.className = 'copy-code-button btn btn-sm'
  button.innerHTML = "<i class='fa-regular fa-copy' aria-hidden='true'></i>"
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(codeBlock.innerText)
      button.title = '복사했습니다'
    } catch {
      button.title = '코드를 선택해 복사해 주세요'
    }
    button.setAttribute('aria-label', button.title)
  })
  const pre = codeBlock.parentNode
  const container = pre.parentNode.classList.contains('highlight') ? pre.parentNode : pre
  container.before(button)
})
