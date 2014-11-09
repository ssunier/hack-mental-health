// Gets epoch time stamp : url visited for the previous day

// Given an array of URLs, build a DOM list of those URLs in the
// browser action popup.
function buildPopupDom(divName, data, data2, json) {
  var popupDiv = document.getElementById(divName);
//    popupDiv.textContent = json;

var xhr = new XMLHttpRequest();
var data = new FormData();
data.append("data" , json);

var xhr = (window.XMLHttpRequest) ? new XMLHttpRequest() : new activeXObject("Microsoft.XMLHTTP");


xhr.open( 'post', '/Users/Joy/Documents/hack-mental-health/hack_health/hack_health/', true );


xhr.send(data);
popupDiv.textContent = 'here';
//chrome.runtime.getPackageDirectoryEntry(function(DirectoryEntry){    popupDiv.textContent = DirectoryEntry.fullPath;})

}

// Search history to find up to ten links that a user has typed in,
// and show those links in a popup.
function buildTypedUrlList(divName) {
  // To look for history items visited in the last week,
  // subtract a week of microseconds from the current time.
  var microsecondsPerDay = 1000 * 60 * 60 * 24;
  var oneDayAgo = (new Date).getTime() - microsecondsPerDay;

  // Track the number of callbacks from chrome.history.getVisits()
  // that we expect to get.  When it reaches zero, we have all results.
  var numRequestsOutstanding = 0;

  chrome.history.search({
      'text': '',              // Return every history item....
      'startTime': oneDayAgo,  // that was accessed less than one week ago.
      'maxResults':100
    },
    function(historyItems) {
      // For each history item, get details on all visits.
      for (var i = 0; i < historyItems.length; ++i) {
        var url = historyItems[i].url;
        var processVisitsWithUrl = function(url) {
          // We need the url of the visited item to process the visit.
          // Use a closure to bind the  url into the callback's args.
          return function(visitItems) {
            processVisits(url, visitItems);
          };
        };
        chrome.history.getVisits({url: url}, processVisitsWithUrl(url));
        numRequestsOutstanding++;
      }
      if (!numRequestsOutstanding) {
        onAllVisitsProcessed();
      }
    });


  // Maps URLs to a count of the number of times the user typed that URL into
  // the omnibox.
  var datestamps = [];
  var urls = [];
  var jsonstring=[];

  // Callback for chrome.history.getVisits().  Counts the number of
  // times a user visited a URL by typing the address.
  var processVisits = function(url, visitItems) {
    for (var i = 0, ie = visitItems.length; i < ie; ++i) {
      // Ignore items unless the user typed the URL.
      //if (visitItems[i].transition != 'typed') {
      //  continue;
      //}
      //  var date = new Date(visitItems[i].visitTime);
      datestamps.push(visitItems[i].visitTime);
      urls.push(url);
      jsonstring+=visitItems[i].visitTime + ':' + url + ',';
    }

    // If this is the final outstanding call to processVisits(),
    // then we have the final results.  Use them to build the list
    // of URLs to show in the popup.
    if (!--numRequestsOutstanding) {
      onAllVisitsProcessed();
    }
  };

  // This function is called when we have the final list of URls to display.
  var onAllVisitsProcessed = function() {
    var json = '{' + jsonstring.slice(0, jsonstring.length-1) + '}';
    buildPopupDom(divName, datestamps, urls, json);
  };
}

document.addEventListener('DOMContentLoaded', function () {
  buildTypedUrlList("typedUrl_div");
});

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
