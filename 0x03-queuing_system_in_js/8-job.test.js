/**
 * Testing the Job creation function.
 */

import { createQueue } from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = createQueue();

describe('test job creation', function () {
  before(function () {
    queue.testMode.enter();
  });
  afterEach(function () {
    queue.testMode.clear();
  });
  after(function () {
    queue.testMode.exit();
  });

  it('testing', function () {
    createPushNotificationsJobs([{ id: 1, phoneNumber: '1234' }, { id: 2, phoneNumber: '1235' }], queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql({ id: 2, phoneNumber: '1235' });
    expect(queue.testMode.jobs[0].data).to.eql({ id: 1, phoneNumber: '1234' });
  });
});
