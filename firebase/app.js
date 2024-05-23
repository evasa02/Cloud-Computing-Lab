// Your web app's Firebase configurationl
const firebaseConfig = {
  apiKey: "AIzaSyBP-PFqsitVLXpqaHSCyc46kDVhwAeyE8A",
  authDomain: "asdfghj-d59da.firebaseapp.com",
  projectId: "asdfghj-d59da",
  storageBucket: "asdfghj-d59da.appspot.com",
  messagingSenderId: "569834652511",
  appId: "1:569834652511:web:08cd2df15a5f8b321cecea",
  measurementId: "G-LMVQDRDYKF"
};
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
  
  // Initialize Firestore
  const db = firebase.firestore();
  
  // Reference to the form
  const dataForm = document.getElementById('dataForm');
  
  // Listen for form submit
  dataForm.addEventListener('submit', (e) => {
    e.preventDefault();
  
    // Get input values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
  
    // Save data to Firestore
    db.collection('users').add({
      name: name,
      email: email,
      timestamp: firebase.firestore.FieldValue.serverTimestamp()
    })
    .then(() => {
      alert('Data saved successfully!');
      dataForm.reset();
    })
    .catch((error) => {
      console.error('Error writing document: ', error);
      alert('Error writing document: ' + error.message);
    });
  });
  