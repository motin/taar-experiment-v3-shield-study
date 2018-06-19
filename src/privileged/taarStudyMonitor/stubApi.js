/* eslint-disable */

ChromeUtils.import("resource://gre/modules/ExtensionCommon.jsm");
ChromeUtils.import("resource://gre/modules/ExtensionUtils.jsm");

// eslint-disable-next-line no-undef
const { EventManager } = ExtensionCommon;
// eslint-disable-next-line no-undef
const { EventEmitter } = ExtensionUtils;

this.taarStudyMonitor = class extends ExtensionAPI {
  getAPI(context) {
    return {
      taarStudyMonitor: {
        /* @TODO no description given */
        onFirstRunOnly: async function onFirstRunOnly() {
          console.log("called onFirstRunOnly ");
          return undefined;
        },

        /* @TODO no description given */
        enableTaarInDiscoPane: async function enableTaarInDiscoPane(
          variationName,
        ) {
          console.log("called enableTaarInDiscoPane variationName");
          return undefined;
        },

        /* @TODO no description given */
        monitorAddonChanges: async function monitorAddonChanges() {
          console.log("called monitorAddonChanges ");
          return undefined;
        },

        /* @TODO no description given */
        setAndPersistClientStatus: async function setAndPersistClientStatus(
          key,
          value,
        ) {
          console.log("called setAndPersistClientStatus key, value");
          return undefined;
        },

        /* @TODO no description given */
        getClientStatus: async function getClientStatus() {
          console.log("called getClientStatus ");
          return undefined;
        },

        /* @TODO no description given */
        incrementAndPersistClientStatusAboutAddonsActiveTabSeconds: async function incrementAndPersistClientStatusAboutAddonsActiveTabSeconds() {
          console.log(
            "called incrementAndPersistClientStatusAboutAddonsActiveTabSeconds ",
          );
          return undefined;
        },

        /* @TODO no description given */
        reset: async function reset() {
          console.log("called reset ");
          return undefined;
        },

        // https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/events.html
        /* Fires when addon-changes are ready to be reported via telemetry. */
        onAddonChangeTelemetry: new EventManager(
          context,
          "taarStudyMonitor:onAddonChangeTelemetry",
          fire => {
            const callback = value => {
              fire.async(value);
            };
            // RegisterSomeInternalCallback(callback);
            return () => {
              // UnregisterInternalCallback(callback);
            };
          },
        ).api(),
      },
    };
  }
};
