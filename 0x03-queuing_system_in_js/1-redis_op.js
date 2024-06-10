/**
 * Connect to redis using node-redis.
 */

import { createClient, print } from 'redis';

const client = await createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) { throw Error(err); }
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
