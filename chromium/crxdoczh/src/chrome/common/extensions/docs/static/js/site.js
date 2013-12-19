(function() {

function addGplusButton() {
  window.___gcfg = {
    lang: 'zh-CN'
  };
  var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
  po.src = 'https://apis.google.com/js/plusone.js?onload=onLoadCallback';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
}

function openFeedback(e) {
  e.preventDefault();
  userfeedback.api.startFeedback({productId: 86265});
}

function addGoogleFeedback() {
  [].forEach.call(document.querySelectorAll('[data-feedback]'), function(el, i) {
    el.addEventListener('click', openFeedback);
  });
}


// Auto syntax highlight all pre tags.
function prettyPrintCode() {
  var pres = document.querySelectorAll('pre');
  for (var i = 0, pre; pre = pres[i]; ++i) {
    pre.classList.add('prettyprint');
  }
  window.prettyPrint && prettyPrint();
}

function setupGotoOriginalLink() {
  document.getElementById('goto-original').href =
      "https://developer.chrome.com" + location.pathname;
}

prettyPrintCode();
//addGoogleFeedback();
addGplusButton();
setupGotoOriginalLink();

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-25062424-1']);
_gaq.push(['_trackPageview']);

(function() {
  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = 'https://ssl.google-analytics.com/ga.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();

})();
