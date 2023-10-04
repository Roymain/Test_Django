fetch('https://pokeapi.co/api/v2/pokemon?offset=0&limit=150')
	.then(response => response.json())
	.then(data => {
		const pokemons = data.results;
		const moviesList = document.getElementById('list');

		pokemons.forEach(pokemon => {

			const listItem = document.createElement('li');		
			listItem.classList.add('in');
			listItem.textContent = pokemon.name;
			moviesList.appendChild(listItem);

		});
	})
	.catch(error => {
	console.error('Une erreur s\'est produite', error);
});
