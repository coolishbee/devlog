const label = 'Copy code'

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
      button.title = 'Copied'
    } catch {
      button.title = 'Select the code to copy'
    }
    button.setAttribute('aria-label', button.title)
  })
  const pre = codeBlock.parentNode
  const container = pre.parentNode.classList.contains('highlight') ? pre.parentNode : pre
  container.before(button)
})
