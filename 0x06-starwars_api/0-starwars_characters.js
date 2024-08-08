#!/usr/bin/env node

const request = require('request');

// Function to fetch data from a URL
function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      if (response.statusCode !== 200) {
        return reject(new Error('Failed to load data, status code: ' + response.statusCode));
      }
      resolve(JSON.parse(body));
    });
  });
}

// Function to print all characters of a movie by ID
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

// Main script
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
