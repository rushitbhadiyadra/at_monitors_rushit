const Sentry = require("@sentry/node");

Sentry.init({
  dsn: process.env.SENTRY_DSN
  // other configuration
});

Sentry.captureException(new Error("GitHub Action failed!"));
