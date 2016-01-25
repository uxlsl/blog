$.event.special.copy.options.trustedDomains = ["*"];
jQuery(document).ready(function($) {
    $("body")
    .on("copy", ".down-url", function(/* ClipboardEvent */ e) {
      var text = $(this).data("zclip-text");
        e.clipboardData.clearData();
      e.clipboardData.setData("text/plain", text);
        e.preventDefault();
        alert("Copied download address to clipboard:\n\n " + text);
      });
  });
