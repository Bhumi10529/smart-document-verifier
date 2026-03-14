async function uploadDocument() {

    const fileInput = document.getElementById("fileInput");

    if (!fileInput.files.length) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
    

    try {

        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log("Backend response:", data);

        alert("File uploaded successfully");

    } catch (error) {

        console.error(error);
        alert("Error connecting to backend");

    }

}