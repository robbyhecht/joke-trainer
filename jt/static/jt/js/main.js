function flipTheCard(card) {
  let flipcard = document.getElementById(card)
  flipcard.classList.toggle('flipit')
}

function deletionModal(modal) {
  let deletion = document.getElementById(modal)
  deletion.classList.add('is-active')
}

function closeDeletionModal(modal) {
  let closeDeletion = document.getElementById(modal)
  closeDeletion.classList.remove('is-active')
}