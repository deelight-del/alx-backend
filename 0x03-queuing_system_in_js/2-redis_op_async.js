/**
 * Connect to redis using node-redis.
 */

import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = await createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool (schoolName, value) {
  try {
    console.log('Reply:', await setAsync(schoolName, value));
  } catch (error) {
    console.log(error);
  }
}

async function displaySchoolValue (schoolName) {
  try {
    console.log(await getAsync(schoolName));
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
