(()=>{"use strict";!function(){const e=new Promise((e=>{if("interactive"===document.readyState||"complete"===document.readyState)return e();document.addEventListener("DOMContentLoaded",(()=>{e()}),{capture:!0,once:!0,passive:!0})}));new Promise((n=>{e.then((()=>fetch("/_/readthedocs-config.json",{method:"GET"}).then((e=>{if(e.ok)return e.json();console.debug("Error parsing configuration data")})))).then((e=>function(e){return new Promise(((n,r)=>{let t=`\n<div class="admonition warning">\n  <p class="admonition-title">Warning</p>\n  <p>\n    This page\n    <a class="reference external" href="${window.location.protocol}//${e.domains.dashboard}/projects/${e.project.slug}/builds/${e.build.id}/">was created </a>\n    from a pull request\n    (<a class="reference external" href="${e.project.repository_url}/pull/${e.version.slug}">#${e.version.slug}</a>).\n  </p>\n</div>\n`,o=document.querySelector("[role=main]")||document.querySelector("#main"),i=document.createElement("div");i.innerHTML=t,o.insertBefore(i,o.firstChild)}))}(e))).then((()=>{n()})).catch((e=>{console.error(e.message)}))}))}()})();
