document.getElementById('city-input').addEventListener('input', function(event) {
    const suggestionsContainer = document.getElementById("suggestions_container");
    const value = event.target.value;
    fetch('/suggestion', {
        method: "POST",
        mode: "cors",
        headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
        },
        body: JSON.stringify({ text: value })
    })
    .then(response => response.json())
    .then(data => {
        suggestionsContainer.innerHTML = "";

        data.forEach(suggestion => {
            const li = document.createElement("li");
            li.innerHTML = suggestion.value;
            li.onclick = function () {
                event.target.value = suggestion.value;
                suggestionsContainer.innerHTML = "";
            };
            suggestionsContainer.appendChild(li);
        });
    });
});
