async function getTweets(apiUrl) {
    const response = await fetch(apiUrl);
    const data = await response.json();
    return data.data;
  }
  
  async function renderTweets(apiUrl) {
    const tweets = await getTweets(apiUrl);
    const tweetContainer = document.getElementById("tweet-container");
  
    tweetContainer.innerHTML = "";
  
    tweets.forEach((tweet) => {
      const tweetElement = document.createElement("div");
      tweetElement.classList.add("tweet");
  
      const tweetId = tweet.url.split("/").pop();
      const tweetEmbedElement = document.createElement("div");
      tweetEmbedElement.classList.add("tweet__embed");
      tweetEmbedElement.dataset.tweetId = tweetId;
      tweetElement.appendChild(tweetEmbedElement);
  
      tweetContainer.appendChild(tweetElement);
  
      twttr.widgets.createTweet(tweetId, tweetEmbedElement);
    });
  }
  
  setInterval(() => {
    renderTweets(apiUrl);
  }, 60000);
  