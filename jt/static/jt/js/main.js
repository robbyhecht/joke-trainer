// EVENT HANDLERS

// handles flashcard flipping
function flipTheCard(card) {
  let flipcard = document.getElementById(card)
  flipcard.classList.toggle('flipit')
}

// handles opening delete modal
function deletionModal(modal) {
  let deletion = document.getElementById(modal)
  deletion.classList.add('is-active')
}

// handles closing delete modal
function closeDeletionModal(modal) {
  let closeDeletion = document.getElementById(modal)
  closeDeletion.classList.remove('is-active')
}