let btn = document.getElementById("btn");
let txt_field = document.getElementById("summary-p");

btn.addEventListener("click", () => {
    txt_field.textContent = "";
    const fileInput = document.getElementById('file');

    // Create a FormData object
    const formData = new FormData();
    
    // Append the selected file to the FormData object
    formData.append('file', fileInput.files[0]);

    // Send the FormData object to the server using fetch
    fetch('http://localhost:5000/summarize', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
    .then(response => {
        let text = response.text;
        
        words = text.split(" ");
        setTextWordByWord(txt_field, words, 0);

    })
    .catch(error => {
        // Handle error
        console.error('Error uploading file:', error);
    });
})

function setTextWordByWord(pTag, words, index) {
    if (index < words.length) {
      setTimeout(function() {
        pTag.textContent += words[index] + " ";
        setTextWordByWord(pTag, words, index + 1);
      }, 150); // Delay of 100 milliseconds (0.1 second)
    }
  }

