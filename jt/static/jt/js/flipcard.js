function flipTheCard(card) {
  let flipcard = document.getElementById(card)
  flipcard.classList.toggle('flipit')
}

function deletionModal(modal) {
  let deletion = document.getElementById(modal)
  deletion.classList.toggle('is-active')
}