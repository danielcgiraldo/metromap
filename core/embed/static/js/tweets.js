// Esta función hace una solicituda la API y devuelve los datos en un arreglo
async function getTweets(apiUrl) {
    const response = await fetch(apiUrl);
    const data = await response.json();
    return data.data;
  }
  
  // Obtienemos los tweets de la API, los renderizamos en el HTML, 
  // y los actualizamos cada 60 segundos
  async function renderTweets(apiUrl) {
    // Obtienemos los tweets utilizando la función getTweets()
    const tweets = await getTweets(apiUrl);
    // Llamamos a "tweet-container" del HTML
    const tweetContainer = document.getElementById("tweet-container");
    // Vaciamos el contenido del "tweet-container" para poder reutilizar la función
    tweetContainer.innerHTML = "";
  
     // Iteramos sobre los tweets y los renderizamos en el HTML
    tweets.forEach((tweet) => {
      // Creamos un <div> en el HTML para el tweet
      const tweetElement = document.createElement("div");
      tweetElement.classList.add("tweet");
  
      // Obtienemos el ID del tweet a partir de la URL
      const tweetId = tweet.url.split("/").pop();
      const tweetEmbedElement = document.createElement("div");
      tweetEmbedElement.classList.add("tweet__embed");
      tweetEmbedElement.dataset.tweetId = tweetId;
      // Agregamos el <div> del tweet embebido al <div> del tweet
      tweetElement.appendChild(tweetEmbedElement);
  
      // Agregamos el <div> del tweet al "tweet-container"
      tweetContainer.appendChild(tweetElement);
  
      // Utilizamos la librería de widgets de Twitter para cargar 
      // el tweet embebido en el <div> correspondiente
      twttr.widgets.createTweet(tweetId, tweetEmbedElement);
    });
  }
  
  // Esta función actualiza la lista de tweets cada 60 segundos
  // por si se publicó uno nuevo
  setInterval(() => {
    renderTweets(apiUrl);
  }, 60000);