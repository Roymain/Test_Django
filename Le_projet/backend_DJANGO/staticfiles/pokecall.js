fetch('https://pokeapi.co/api/v2/pokemon?offset=0&limit=60')
  .then(response => response.json())
  .then(data => {
    console.log(data.results);

    const movies = data.results;
        const moviesList = document.getElementById('mon_param');

        movies.forEach(movie => {
          const link = document.createElement('a');
          const listItem = document.createElement('li');
          const dot = document.createElement('span');
            
          link.classList.add('red-dot');
          listItem.classList.add('list');
          dot.classList.add('dot');
          listItem.textContent = movie.name;
          link.href = `https://pokeapi.co/api/v2/pokemon/${movie.name}`;
          link.appendChild(dot);
          listItem.appendChild(link);
          moviesList.appendChild(listItem);
        });
  })
  .catch(error => {
    console.error('Une erreur s\'est produite', error);
});

