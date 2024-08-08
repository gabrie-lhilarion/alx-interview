#!/usr/bin/env node

const https = require('https');

function fetch (url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        resolve(JSON.parse(data));
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
}

async function printMovieCharacters (movieId) {
  try {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
    const movieData = await fetch(movieUrl);

    const characters = movieData.characters;

    for (const characterUrl of characters) {
      const characterData = await fetch(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = parseInt(process.argv[2]);

if (isNaN(movieId)) {
  console.log('Movie ID must be an integer.');
  process.exit(1);
}

printMovieCharacters(movieId);
