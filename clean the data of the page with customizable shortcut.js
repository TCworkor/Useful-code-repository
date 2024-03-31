// ==UserScript==
// @name         sand_time
// @namespace    http://tampermonkey.net/
// @version      1.6
// @description  clean the data of the page with customizable shortcut
// @author       TCworkor
// @match        https://*/*
// @match        http://*/*
// @icon         https://cdn4.iconfinder.com/data/icons/general-office/91/General_Office_47-64.png
// @grant        GM_registerMenuCommand
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

(function() {
    'use strict';

    // Function to clear website data
    function clearWebsiteData() {
        document.cookie.split(';').forEach(function(c) {
            document.cookie = c.trim().split('=')[0] + '=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
        });
        localStorage.clear();
        sessionStorage.clear();
        window.location.reload();
    }

    // Register menu commands
    GM_registerMenuCommand("Clear Website Data", clearWebsiteData);
    GM_registerMenuCommand("Set Custom Shortcut for Clearing Data", setCustomShortcut);

    // Function to set custom shortcut
    function setCustomShortcut() {
        let currentShortcut = GM_getValue("customShortcut", "Ctrl+Shift+X");
        let userShortcut = prompt("Enter your custom shortcut for clearing website data:", currentShortcut);
        if (userShortcut) {
            GM_setValue("customShortcut", userShortcut);
            alert("Custom shortcut set to: " + userShortcut);
        }
    }

    // Add a keyboard shortcut to clear website data
    document.addEventListener('keydown', function(e) {
        let customShortcut = GM_getValue("customShortcut", "Ctrl+Shift+X");
        let keys = customShortcut.split("+");
        let ctrlKeyNeeded = keys.includes("Ctrl");
        let shiftKeyNeeded = keys.includes("Shift");
        let key = keys.find(k => k !== "Ctrl" && k !== "Shift");

        if (
            (e.ctrlKey === ctrlKeyNeeded || !ctrlKeyNeeded) &&
            (e.shiftKey === shiftKeyNeeded || !shiftKeyNeeded) &&
            e.key === key
        ) {
            clearWebsiteData();
        }
    });
})();
