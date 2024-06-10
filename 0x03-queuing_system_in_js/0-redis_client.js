/**
 * Connect to redis using node-redis.
 */

import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

