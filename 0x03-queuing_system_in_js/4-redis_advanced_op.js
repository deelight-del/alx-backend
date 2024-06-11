/*
 * Storing hash values with redis client.
 */

import { createClient, print } from 'redis';

const client = await createClient()
  .on('error', err => console.log(`Redis client not connnected to the server: ${error}`))
  .on('connect', () => console.log('Redis client connected to the server'));

client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

client.hgetall('HolbertonSchools', (err, data) => {
  if (err) { throw new Error(err); }
  console.log(data);
});
