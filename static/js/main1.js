function myFunction(){
    window.location.href = "/secondpage";
}

function anotherfunction(){
    window.location.href = "/";
}
function thirdpage()
{
    window.location.href = "/thirdpage";
}

function search(){
    var query = document.getElementById('query').value;
    console.log('Query value:', query);
    fetch('/thirdpage',  {
    method: 'POST', 
    headers:     {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'query=' + encodeURIComponent(query)
    })
    .then(response=> response.json())
    .then(data => {
        console.log('Received data:', data); 
        var resultsDiv = document.getElementById('search-results');
        resultsDiv.innerHTML = '<h3>Search Results:</h3>';
        if(data.length > 0) 
        {
            for(var i = 0; i < data.length; i++)
            {
                resultsDiv.innerHTML += '<p><strong>Exchange:</strong>' + data[i].exchange + '</p>';
                resultsDiv.innerHTML += '<p><strong>Short Name:</strong> ' + data[i].shortname + '</p>';
                resultsDiv.innerHTML += '<p><strong>Symbol:</strong> ' + data[i].symbol + '</p>';
                resultsDiv.innerHTML += '<p><strong>Industry:</strong> ' + data[i].industry + '</p>';
                resultsDiv.innerHTML += '<p><strong>Score:</strong> ' + data[i].score + '</p>';

            }
        }
        else {
                resultsDiv.innerHTML += '<p>No results found.</p>'; 
            }
        
    })
    .catch(error => {
        console.error('Error Fetching search results:', error); 
    }
        )


}

    
    
    
