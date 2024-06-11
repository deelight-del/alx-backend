/*eslint-disable*/

/**
 * Create a job with the
 * Kue module.
 */

import { createQueue } from 'kue';

const push_notification_code = createQueue();

const newObj = {
  phoneNumber: '08055771123',
  message: 'Let\'s go a fishing'
};

const job = push_notification_code.create('push_notification_code', newObj).save(function (err) {
  if (!err) { console.log(`Notification job created ${job.id}`); }
});

job.on('complete', (result) => { console.log('Notification job completed'); });

job.on('failed', (errMessage) => { console.log('Notification job failed'); });
