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
    fetch('/search',  {
    method: 'POST', 
    headers:     {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'query=' + encodeURIComponent(query)

    })

    .then(response=> response.json())
    .then(data => {
        var resultsDiv = document.getElementById('search-results');
        resultsDiv.innerHTML = '<h3>Search Results:</h3>';
        if(data.length > 0) 
        {
            for(var i = 0; i < data.length; i++)
            {
                resultsDiv.innerHTML += '<p>' + data[i] + '</p>';

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

    
    
    
