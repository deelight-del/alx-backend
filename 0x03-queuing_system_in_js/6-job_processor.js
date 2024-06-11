/**
 * Process the job that was initially created
 * using in '6-job_creator.js'
 */

import { createQueue } from 'kue';
const queue = createQueue();

function sendNotification (phoneNumber, message) {
  console.log(`Sending Notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
