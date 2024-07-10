#!/usr/bin/node

const filmID = process.argv[2]
const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

request(apiUrl, (error, response, body) => {

    if (error) {
        throw error;
    }

    let json = JSON.parse(body);
    let characters = json.characters

    characters.map((character) => {
        const characterAPI = character;

        request(characterAPI, (error, response, body) => {
            const characterJSON = JSON.parse(body);
            console.log(characterJSON.name)
        })
    })
});
