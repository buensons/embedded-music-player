let files = [];

function loadFiles() {
    fetch('http://127.0.0.1:8888/files', {
	method: 'GET',
	mode: 'cors'
    }).then((response) => {
        return response.json();
    }).then((data) => {
        displayFiles(data);
    });
}

function displayFiles(data) {
    for(let i = 0; i < data.length; i++) {
        files.push(data[i]);
        document.getElementById("main").innerHTML +=
            '<form action="/download" method="POST">'
            + '<input type="hidden" name="file" value="' + data[i] + '"/>'
            + '<input type="submit" value="Download"/>'
            + '</form>'
            + '<form action="/delete" method="POST">'
            + '<input type="hidden" name="file" value="' + data[i] + '"/>'
            + '<input type="submit" value="Remove"/>'
            + '</form>'
            // + '<button onclick="download(\'' + i + '\')">Download</button>'
            + '<span style="margin-left:50px;">' 
            + data[i] + "</span><br>";
    }
}

function download(index) {
    window.open("/download/" + files[index]);
}

function logout() {
    window.location = "/logout";
}

loadFiles();
