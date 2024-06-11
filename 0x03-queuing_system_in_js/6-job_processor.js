import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process for job processing
queue.process('push_notification_code', (job, done) => {
  // Access job data
  const { phoneNumber, message } = job.data;
  
  // Call sendNotification function with job data
  sendNotification(phoneNumber, message);

  // Mark job as completed
  done();
});
