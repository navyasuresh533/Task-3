Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> import requests
>>> url='https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
>>> page = requests.get(url)
>>> soup = BeautifulSoup(page.text, 'html')
>>> print(soup)
<!DOCTYPE html>

<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-enabled vector-feature-appearance-pinned-clientpref-1 vector-feature-night-mode-disabled skin-theme-clientpref-day vector-toc-available" dir="ltr" lang="en">
<head>
<meta charset="utf-8"/>
<title>List of largest companies by revenue - Wikipedia</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-enabled vector-feature-appearance-pinned-clientpref-1 vector-feature-night-mode-disabled skin-theme-clientpref-day vector-toc-available";var cookie=document.cookie.match(/(?:^|; )enwikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":[
"",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"ac1766d9-493f-436b-85ca-c60df63d50d4","wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"List_of_largest_companies_by_revenue","wgTitle":"List of largest companies by revenue","wgCurRevisionId":1225623550,"wgRevisionId":1225623550,"wgArticleId":997455,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Articles with short description","Short description is different from Wikidata","Lists of companies by revenue","Economy-related lists of superlatives"],"wgPageViewLanguage":"en","wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"List_of_largest_companies_by_revenue","wgRelevantArticleId":997455,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,
"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoticeProject":"wikipedia","wgCiteReferencePreviewsActive":false,"wgFlaggedRevsParams":{"tags":{"status":{"levels":1}}},"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsFlags":6,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":false,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":30000,"wgULSCurrentAutonym":"English","wgCentralAuthMobileDomain":false,"wgEditSubmitButtonLabelPublish":true,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,"wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgWikibaseItemId":"Q900297","wgCheckUserClientHintsHeadersJsApi":["architecture","bitness","brands","fullVersionList","mobile","model","platform","platformVersion"],"GEHomepageSuggestedEditsEnableTopics":true,"wgGETopicsMatchModeEnabled":
false,"wgGEStructuredTaskRejectionReasonTextInputEnabled":false,"wgGELevelingUpEnabledForUser":false};RLSTATE={"ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.cite.styles":"ready","skins.vector.search.codex.styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","jquery.tablesorter.styles":"ready","jquery.makeCollapsible.styles":"ready","ext.wikimediamessages.styles":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","wikibase.client.init":"ready","ext.wikimediaBadges":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","mediawiki.page.media","site","mediawiki.page.ready","jquery.tablesorter","jquery.makeCollapsible","mediawiki.toc","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.ReferenceTooltips","ext.gadget.switcher","ext.urlShortener.toolbar",
"ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.echo.centralauth","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.cx.uls.quick.actions","wikibase.client.vector-2022","ext.checkUser.clientHints","ext.growthExperiments.SuggestedEditSession"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
}];});});</script>
<link href="/w/load.php?lang=en&amp;modules=ext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cext.wikimediamessages.styles%7Cjquery.makeCollapsible.styles%7Cjquery.tablesorter.styles%7Cskins.vector.icons%2Cstyles%7Cskins.vector.search.codex.styles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector-2022" rel="stylesheet"/>
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector-2022"></script>
<meta content="" name="ResourceLoaderDynamicStyles"/>
<link href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector-2022" rel="stylesheet"/>
<meta content="MediaWiki 1.43.0-wmf.11" name="generator"/>
<meta content="origin" name="referrer"/>
<meta content="origin-when-cross-origin" name="referrer"/>
<meta content="max-image-preview:standard" name="robots"/>
<meta content="telephone=no" name="format-detection"/>
<meta content="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/1200px-Walmart_store_exterior_5266815680.jpg" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="901" property="og:image:height"/>
<meta content="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/800px-Walmart_store_exterior_5266815680.jpg" property="og:image"/>
<meta content="800" property="og:image:width"/>
<meta content="601" property="og:image:height"/>
<meta content="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/640px-Walmart_store_exterior_5266815680.jpg" property="og:image"/>
<meta content="640" property="og:image:width"/>
<meta content="481" property="og:image:height"/>
<meta content="width=1120" name="viewport"/>
<meta content="List of largest companies by revenue - Wikipedia" property="og:title"/>
<meta content="website" property="og:type"/>
<link href="//upload.wikimedia.org" rel="preconnect"/>
<link href="//en.m.wikipedia.org/wiki/List_of_largest_companies_by_revenue" media="only screen and (max-width: 640px)" rel="alternate"/>
<link href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit" rel="alternate" title="Edit this page" type="application/x-wiki"/>
<link href="/static/apple-touch/wikipedia.png" rel="apple-touch-icon"/>
<link href="/static/favicon/wikipedia.ico" rel="icon"/>
<link href="/w/rest.php/v1/search" rel="search" title="Wikipedia (en)" type="application/opensearchdescription+xml"/>
<link href="//en.wikipedia.org/w/api.php?action=rsd" rel="EditURI" type="application/rsd+xml"/>
<link href="https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue" rel="canonical"/>
<link href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" rel="license"/>
<link href="/w/index.php?title=Special:RecentChanges&amp;feed=atom" rel="alternate" title="Wikipedia Atom feed" type="application/atom+xml"/>
<link href="//meta.wikimedia.org" rel="dns-prefetch">
<link href="//login.wikimedia.org" rel="dns-prefetch"/>
</link></head>
<body class="skin--responsive skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-List_of_largest_companies_by_revenue rootpage-List_of_largest_companies_by_revenue skin-vector-2022 action-view"><a class="mw-jump-link" href="#bodyContent">Jump to content</a>
<div class="vector-header-container">
<header class="vector-header mw-header">
<div class="vector-header-start">
<nav aria-label="Site" class="vector-main-menu-landmark">
<div class="vector-dropdown vector-main-menu-dropdown vector-button-flush-left vector-button-flush-right" id="vector-main-menu-dropdown">
<input aria-haspopup="true" aria-label="Main menu" class="vector-dropdown-checkbox" data-event-name="ui.dropdown-vector-main-menu-dropdown" id="vector-main-menu-dropdown-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only" for="vector-main-menu-dropdown-checkbox" id="vector-main-menu-dropdown-label"><span class="vector-icon mw-ui-icon-menu mw-ui-icon-wikimedia-menu"></span>
<span class="vector-dropdown-label-text">Main menu</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-unpinned-container" id="vector-main-menu-unpinned-container">
<div class="vector-main-menu vector-pinnable-element" id="vector-main-menu">
<div class="vector-pinnable-header vector-main-menu-pinnable-header vector-pinnable-header-unpinned" data-feature-name="main-menu-pinned" data-pinnable-element-id="vector-main-menu" data-pinned-container-id="vector-main-menu-pinned-container" data-unpinned-container-id="vector-main-menu-unpinned-container">
<div class="vector-pinnable-header-label">Main menu</div>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-main-menu.pin">move to sidebar</button>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-main-menu.unpin">hide</button>
</div>
<div class="vector-menu mw-portlet mw-portlet-navigation" id="p-navigation">
<div class="vector-menu-heading">
		Navigation
	</div>
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="mw-list-item" id="n-mainpage-description"><a accesskey="z" href="/wiki/Main_Page" title="Visit the main page [z]"><span>Main page</span></a></li><li class="mw-list-item" id="n-contents"><a href="/wiki/Wikipedia:Contents" title="Guides to browsing Wikipedia"><span>Contents</span></a></li><li class="mw-list-item" id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Articles related to current events"><span>Current events</span></a></li><li class="mw-list-item" id="n-randompage"><a accesskey="x" href="/wiki/Special:Random" title="Visit a randomly selected article [x]"><span>Random article</span></a></li><li class="mw-list-item" id="n-aboutsite"><a href="/wiki/Wikipedia:About" title="Learn about Wikipedia and how it works"><span>About Wikipedia</span></a></li><li class="mw-list-item" id="n-contactpage"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us" title="How to contact Wikipedia"><span>Contact us</span></a></li><li class="mw-list-item" id="n-sitesupport"><a href="https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us by donating to the Wikimedia Foundation"><span>Donate</span></a></li>
</ul>
</div>
</div>
<div class="vector-menu mw-portlet mw-portlet-interaction" id="p-interaction">
<div class="vector-menu-heading">
		Contribute
	</div>
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="mw-list-item" id="n-help"><a href="/wiki/Help:Contents" title="Guidance on how to use and edit Wikipedia"><span>Help</span></a></li><li class="mw-list-item" id="n-introduction"><a href="/wiki/Help:Introduction" title="Learn how to edit Wikipedia"><span>Learn to edit</span></a></li><li class="mw-list-item" id="n-portal"><a href="/wiki/Wikipedia:Community_portal" title="The hub for editors"><span>Community portal</span></a></li><li class="mw-list-item" id="n-recentchanges"><a accesskey="r" href="/wiki/Special:RecentChanges" title="A list of recent changes to Wikipedia [r]"><span>Recent changes</span></a></li><li class="mw-list-item" id="n-upload"><a href="/wiki/Wikipedia:File_upload_wizard" title="Add images or other media for use on Wikipedia"><span>Upload file</span></a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</nav>
<a class="mw-logo" href="/wiki/Main_Page">
<img alt="" aria-hidden="true" class="mw-logo-icon" height="50" src="/static/images/icons/wikipedia.png" width="50"/>
<span class="mw-logo-container skin-invert">
<img alt="Wikipedia" class="mw-logo-wordmark" src="/static/images/mobile/copyright/wikipedia-wordmark-en.svg" style="width: 7.5em; height: 1.125em;"/>
<img alt="The Free Encyclopedia" class="mw-logo-tagline" height="13" src="/static/images/mobile/copyright/wikipedia-tagline-en.svg" style="width: 7.3125em; height: 0.8125em;" width="117"/>
</span>
</a>
</div>
<div class="vector-header-end">
<div class="vector-search-box-vue vector-search-box-collapses vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box" id="p-search" role="search">
<a accesskey="f" class="cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only search-toggle" href="/wiki/Special:Search" title="Search Wikipedia [f]"><span class="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search"></span>
<span>Search</span>
</a>
<div class="vector-typeahead-search-container">
<div class="cdx-typeahead-search cdx-typeahead-search--show-thumbnail cdx-typeahead-search--auto-expand-width">
<form action="/w/index.php" class="cdx-search-input cdx-search-input--has-end-button" id="searchform">
<div class="cdx-search-input__input-wrapper" data-search-loc="header-moved" id="simpleSearch">
<div class="cdx-text-input cdx-text-input--has-start-icon">
<input accesskey="f" aria-label="Search Wikipedia" autocapitalize="sentences" class="cdx-text-input__input" id="searchInput" name="search" placeholder="Search Wikipedia" title="Search Wikipedia [f]" type="search"/>
<span class="cdx-text-input__icon cdx-text-input__start-icon"></span>
</div>
<input name="title" type="hidden" value="Special:Search"/>
</div>
<button class="cdx-button cdx-search-input__end-button">Search</button>
</form>
</div>
</div>
</div>
<nav aria-label="Personal tools" class="vector-user-links vector-user-links-wide">
<div class="vector-user-links-main">
<div class="vector-menu mw-portlet emptyPortlet" id="p-vector-user-menu-preferences">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
</ul>
</div>
</div>
<div class="vector-menu mw-portlet emptyPortlet" id="p-vector-user-menu-userpage">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
</ul>
</div>
</div>
<nav aria-label="Appearance" class="vector-appearance-landmark">
<div class="vector-dropdown" id="vector-appearance-dropdown">
<input aria-haspopup="true" aria-label="Appearance" class="vector-dropdown-checkbox" data-event-name="ui.dropdown-vector-appearance-dropdown" id="vector-appearance-dropdown-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only" for="vector-appearance-dropdown-checkbox" id="vector-appearance-dropdown-label"><span class="vector-icon mw-ui-icon-appearance mw-ui-icon-wikimedia-appearance"></span>
<span class="vector-dropdown-label-text">Appearance</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-unpinned-container" id="vector-appearance-unpinned-container">
</div>
</div>
</div>
</nav>
<div class="vector-menu mw-portlet emptyPortlet" id="p-vector-user-menu-notifications">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
</ul>
</div>
</div>
<div class="vector-menu mw-portlet" id="p-vector-user-menu-overflow">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="user-links-collapsible-item mw-list-item user-links-collapsible-item" id="pt-createaccount-2"><a class="" data-mw="interface" href="/w/index.php?title=Special:CreateAccount&amp;returnto=List+of+largest+companies+by+revenue" title="You are encouraged to create an account and log in; however, it is not mandatory"><span>Create account</span></a>
</li>
<li class="user-links-collapsible-item mw-list-item user-links-collapsible-item" id="pt-login-2"><a accesskey="o" class="" data-mw="interface" href="/w/index.php?title=Special:UserLogin&amp;returnto=List+of+largest+companies+by+revenue" title="You're encouraged to log in; however, it's not mandatory. [o]"><span>Log in</span></a>
</li>
</ul>
</div>
</div>
</div>
<div class="vector-dropdown vector-user-menu vector-button-flush-right vector-user-menu-logged-out" id="vector-user-links-dropdown" title="Log in and more options">
<input aria-haspopup="true" aria-label="Personal tools" class="vector-dropdown-checkbox" data-event-name="ui.dropdown-vector-user-links-dropdown" id="vector-user-links-dropdown-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only" for="vector-user-links-dropdown-checkbox" id="vector-user-links-dropdown-label"><span class="vector-icon mw-ui-icon-ellipsis mw-ui-icon-wikimedia-ellipsis"></span>
<span class="vector-dropdown-label-text">Personal tools</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-menu mw-portlet mw-portlet-personal user-links-collapsible-item" id="p-personal" title="User menu">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="user-links-collapsible-item mw-list-item" id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=List+of+largest+companies+by+revenue" title="You are encouraged to create an account and log in; however, it is not mandatory"><span class="vector-icon mw-ui-icon-userAdd mw-ui-icon-wikimedia-userAdd"></span> <span>Create account</span></a></li><li class="user-links-collapsible-item mw-list-item" id="pt-login"><a accesskey="o" href="/w/index.php?title=Special:UserLogin&amp;returnto=List+of+largest+companies+by+revenue" title="You're encouraged to log in; however, it's not mandatory. [o]"><span class="vector-icon mw-ui-icon-logIn mw-ui-icon-wikimedia-logIn"></span> <span>Log in</span></a></li>
</ul>
</div>
</div>
<div class="vector-menu mw-portlet mw-portlet-user-menu-anon-editor" id="p-user-menu-anon-editor">
<div class="vector-menu-heading">
		Pages for logged out editors <a aria-label="Learn more about editing" href="/wiki/Help:Introduction"><span>learn more</span></a>
</div>
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="mw-list-item" id="pt-anoncontribs"><a accesskey="y" href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]"><span>Contributions</span></a></li><li class="mw-list-item" id="pt-anontalk"><a accesskey="n" href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]"><span>Talk</span></a></li>
</ul>
</div>
</div>
</div>
</div>
</nav>
</div>
</header>
</div>
<div class="mw-page-container">
<div class="mw-page-container-inner">
<div class="vector-sitenotice-container">
<div class="notheme" id="siteNotice"><!-- CentralNotice --></div>
</div>
<div class="vector-column-start">
<div class="vector-main-menu-container">
<div id="mw-navigation">
<nav aria-label="Site" class="vector-main-menu-landmark" id="mw-panel">
<div class="vector-pinned-container" id="vector-main-menu-pinned-container">
</div>
</nav>
</div>
</div>
<div class="vector-sticky-pinned-container">
<nav aria-label="Contents" class="mw-table-of-contents-container vector-toc-landmark" data-event-name="ui.sidebar-toc" id="mw-panel-toc">
<div class="vector-pinned-container" id="vector-toc-pinned-container">
<div class="vector-toc vector-pinnable-element" id="vector-toc">
<div class="vector-pinnable-header vector-toc-pinnable-header vector-pinnable-header-pinned" data-feature-name="toc-pinned" data-pinnable-element-id="vector-toc">
<h2 class="vector-pinnable-header-label">Contents</h2>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-toc.pin">move to sidebar</button>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-toc.unpin">hide</button>
</div>
<ul class="vector-toc-contents" id="mw-panel-toc-list">
<li class="vector-toc-list-item vector-toc-level-1" id="toc-mw-content-text">
<a class="vector-toc-link" href="#">
<div class="vector-toc-text">(Top)</div>
</a>
</li>
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-List">
<a class="vector-toc-link" href="#List">
<div class="vector-toc-text">
<span class="vector-toc-numb">1</span>
<span>List</span>
</div>
</a>
<ul class="vector-toc-list" id="toc-List-sublist">
</ul>
</li>
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-By_country">
<a class="vector-toc-link" href="#By_country">
<div class="vector-toc-text">
<span class="vector-toc-numb">2</span>
<span>By country</span>
</div>
</a>
<ul class="vector-toc-list" id="toc-By_country-sublist">
</ul>
</li>
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-Notes">
<a class="vector-toc-link" href="#Notes">
<div class="vector-toc-text">
<span class="vector-toc-numb">3</span>
<span>Notes</span>
</div>
</a>
<ul class="vector-toc-list" id="toc-Notes-sublist">
</ul>
</li>
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-See_also">
<a class="vector-toc-link" href="#See_also">
<div class="vector-toc-text">
<span class="vector-toc-numb">4</span>
<span>See also</span>
</div>
</a>
<ul class="vector-toc-list" id="toc-See_also-sublist">
</ul>
</li>
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-References">
<a class="vector-toc-link" href="#References">
<div class="vector-toc-text">
<span class="vector-toc-numb">5</span>
<span>References</span>
</div>
</a>
<ul class="vector-toc-list" id="toc-References-sublist">
</ul>
</li>
<li class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded" id="toc-External_links">
<a class="vector-toc-link" href="#External_links">
<div class="vector-toc-text">
<span class="vector-toc-numb">6</span>
<span>External links</span>
</div>
</a>
<ul class="vector-toc-list" id="toc-External_links-sublist">
</ul>
</li>
</ul>
</div>
</div>
</nav>
</div>
</div>
<div class="mw-content-container">
<main class="mw-body" id="content">
<header class="mw-body-header vector-page-titlebar">
<nav aria-label="Contents" class="vector-toc-landmark">
<div class="vector-dropdown vector-page-titlebar-toc vector-button-flush-left" id="vector-page-titlebar-toc">
<input aria-haspopup="true" aria-label="Toggle the table of contents" class="vector-dropdown-checkbox" data-event-name="ui.dropdown-vector-page-titlebar-toc" id="vector-page-titlebar-toc-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only" for="vector-page-titlebar-toc-checkbox" id="vector-page-titlebar-toc-label"><span class="vector-icon mw-ui-icon-listBullet mw-ui-icon-wikimedia-listBullet"></span>
<span class="vector-dropdown-label-text">Toggle the table of contents</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-unpinned-container" id="vector-page-titlebar-toc-unpinned-container">
</div>
</div>
</div>
</nav>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">List of largest companies by revenue</span></h1>
<div class="vector-dropdown mw-portlet mw-portlet-lang" id="p-lang-btn">
<input aria-haspopup="true" aria-label="Go to an article in another language. Available in 22 languages" class="vector-dropdown-checkbox mw-interlanguage-selector" data-event-name="ui.dropdown-p-lang-btn" id="p-lang-btn-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--action-progressive mw-portlet-lang-heading-22" for="p-lang-btn-checkbox" id="p-lang-btn-label"><span class="vector-icon mw-ui-icon-language-progressive mw-ui-icon-wikimedia-language-progressive"></span>
<span class="vector-dropdown-label-text">22 languages</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="interlanguage-link interwiki-ar mw-list-item"><a class="interlanguage-link-target" href="https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A7%D9%84%D8%B4%D8%B1%D9%83%D8%A7%D8%AA_%D8%AD%D8%B3%D8%A8_%D8%A7%D9%84%D8%AF%D8%AE%D9%84" hreflang="ar" lang="ar" title="قائمة الشركات حسب الدخل – Arabic"><span>العربية</span></a></li><li class="interlanguage-link interwiki-az mw-list-item"><a class="interlanguage-link-target" href="https://az.wikipedia.org/wiki/G%C9%99lirl%C9%99rin%C9%99_g%C3%B6r%C9%99_d%C3%BCnyan%C4%B1n_%C9%99n_b%C3%B6y%C3%BCk_%C5%9Firk%C9%99tl%C9%99rinin_siyah%C4%B1s%C4%B1" hreflang="az" lang="az" title="Gəlirlərinə görə dünyanın ən böyük şirkətlərinin siyahısı – Azerbaijani"><span>Azərbaycanca</span></a></li><li class="interlanguage-link interwiki-bn mw-list-item"><a class="interlanguage-link-target" href="https://bn.wikipedia.org/wiki/%E0%A6%86%E0%A6%AF%E0%A6%BC_%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%AF%E0%A6%BE%E0%A6%AF%E0%A6%BC%E0%A7%80_%E0%A6%AC%E0%A7%83%E0%A6%B9%E0%A7%8E_%E0%A6%95%E0%A7%8B%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%BE%E0%A6%A8%E0%A6%BF%E0%A6%B0_%E0%A6%A4%E0%A6%BE%E0%A6%B2%E0%A6%BF%E0%A6%95%E0%A6%BE" hreflang="bn" lang="bn" title="আয় অনুযায়ী বৃহৎ কোম্পানির তালিকা – Bangla"><span>বাংলা</span></a></li><li class="interlanguage-link interwiki-cs mw-list-item"><a class="interlanguage-link-target" href="https://cs.wikipedia.org/wiki/Seznam_nejv%C4%9Bt%C5%A1%C3%ADch_sv%C4%9Btov%C3%BDch_firem_podle_tr%C5%BEeb" hreflang="cs" lang="cs" title="Seznam největších světových firem podle tržeb – Czech"><span>Čeština</span></a></li><li class="interlanguage-link interwiki-de mw-list-item"><a class="interlanguage-link-target" href="https://de.wikipedia.org/wiki/Liste_der_gr%C3%B6%C3%9Ften_Unternehmen_der_Welt" hreflang="de" lang="de" title="Liste der größten Unternehmen der Welt – German"><span>Deutsch</span></a></li><li class="interlanguage-link interwiki-es mw-list-item"><a class="interlanguage-link-target" href="https://es.wikipedia.org/wiki/Anexo:Empresas_por_ingresos" hreflang="es" lang="es" title="Anexo:Empresas por ingresos – Spanish"><span>Español</span></a></li><li class="interlanguage-link interwiki-fa mw-list-item"><a class="interlanguage-link-target" href="https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%A8%D8%B2%D8%B1%DA%AF%E2%80%8C%D8%AA%D8%B1%DB%8C%D9%86_%D8%B4%D8%B1%DA%A9%D8%AA%E2%80%8C%D9%87%D8%A7_%D8%A8%D8%B1_%D9%BE%D8%A7%DB%8C%D9%87_%D8%AF%D8%B1%D8%A2%D9%85%D8%AF" hreflang="fa" lang="fa" title="فهرست بزرگ‌ترین شرکت‌ها بر پایه درآمد – Persian"><span>فارسی</span></a></li><li class="interlanguage-link interwiki-fr mw-list-item"><a class="interlanguage-link-target" href="https://fr.wikipedia.org/wiki/Liste_des_plus_grandes_entreprises_par_chiffre_d%27affaires" hreflang="fr" lang="fr" title="Liste des plus grandes entreprises par chiffre d'affaires – French"><span>Français</span></a></li><li class="interlanguage-link interwiki-hy mw-list-item"><a class="interlanguage-link-target" href="https://hy.wikipedia.org/wiki/%D4%B1%D5%B7%D5%AD%D5%A1%D6%80%D5%B0%D5%AB_%D5%A1%D5%B4%D5%A5%D5%B6%D5%A1%D5%A5%D5%AF%D5%A1%D5%B4%D5%BF%D5%A1%D5%A2%D5%A5%D6%80_%D5%A8%D5%B6%D5%AF%D5%A5%D6%80%D5%B8%D6%82%D5%A9%D5%B5%D5%B8%D6%82%D5%B6%D5%B6%D5%A5%D6%80%D5%AB_%D6%81%D5%A1%D5%B6%D5%AF" hreflang="hy" lang="hy" title="Աշխարհի ամենաեկամտաբեր ընկերությունների ցանկ – Armenian"><span>Հայերեն</span></a></li><li class="interlanguage-link interwiki-hi mw-list-item"><a class="interlanguage-link-target" href="https://hi.wikipedia.org/wiki/%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%A4%E0%A4%BF_%E0%A4%95%E0%A5%87_%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0_%E0%A4%AA%E0%A4%B0_%E0%A4%B8%E0%A4%AC%E0%A4%B8%E0%A5%87_%E0%A4%AC%E0%A4%A1%E0%A4%BC%E0%A5%80_%E0%A4%95%E0%A4%82%E0%A4%AA%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A5%8B%E0%A4%82_%E0%A4%95%E0%A5%80_%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A5%80" hreflang="hi" lang="hi" title="संप्राप्ति के आधार पर सबसे बड़ी कंपनियों की सूची – Hindi"><span>हिन्दी</span></a></li><li class="interlanguage-link interwiki-hu mw-list-item"><a class="interlanguage-link-target" href="https://hu.wikipedia.org/wiki/C%C3%A9gek_list%C3%A1ja_bev%C3%A9tel%C3%BCk_alapj%C3%A1n" hreflang="hu" lang="hu" title="Cégek listája bevételük alapján – Hungarian"><span>Magyar</span></a></li><li class="interlanguage-link interwiki-mr mw-list-item"><a class="interlanguage-link-target" href="https://mr.wikipedia.org/wiki/%E0%A4%95%E0%A4%AE%E0%A4%BE%E0%A4%88%E0%A4%A8%E0%A5%81%E0%A4%B8%E0%A4%BE%E0%A4%B0_%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%A4_%E0%A4%AE%E0%A5%8B%E0%A4%A0%E0%A5%8D%E0%A4%AF%E0%A4%BE_%E0%A4%95%E0%A4%82%E0%A4%AA%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%82%E0%A4%9A%E0%A5%80_%E0%A4%AF%E0%A4%BE%E0%A4%A6%E0%A5%80" hreflang="mr" lang="mr" title="कमाईनुसार सर्वात मोठ्या कंपन्यांची यादी – Marathi"><span>मराठी</span></a></li><li class="interlanguage-link interwiki-ne mw-list-item"><a class="interlanguage-link-target" href="https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%AE%E0%A4%BE%E0%A4%87%E0%A4%95%E0%A4%BE_%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%AE%E0%A4%BE_%E0%A4%A0%E0%A5%82%E0%A4%B2%E0%A4%BE_%E0%A4%95%E0%A4%AE%E0%A5%8D%E0%A4%AA%E0%A4%A8%E0%A5%80%E0%A4%B9%E0%A4%B0%E0%A5%82%E0%A4%95%E0%A5%8B_%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A5%80" hreflang="ne" lang="ne" title="कमाइका आधारमा ठूला कम्पनीहरूको सूची – Nepali"><span>नेपाली</span></a></li><li class="interlanguage-link interwiki-pnb mw-list-item"><a class="interlanguage-link-target" href="https://pnb.wikipedia.org/wiki/%D9%88%DA%88%DB%8C%D8%A7%DA%BA_%DA%A9%D9%85%D9%BE%D9%86%D9%8A%D8%A7%DA%BA_%D8%AF%DB%8C_%D9%84%D8%B3%D9%B9_%D8%A8%D9%84%D8%AD%D8%A7%D8%B8_%D8%A2%D9%85%D8%AF%D9%86%DB%8C" hreflang="pnb" lang="pnb" title="وڈیاں کمپنياں دی لسٹ بلحاظ آمدنی – Western Punjabi"><span>پنجابی</span></a></li><li class="interlanguage-link interwiki-pl mw-list-item"><a class="interlanguage-link-target" href="https://pl.wikipedia.org/wiki/Lista_najwi%C4%99kszych_przedsi%C4%99biorstw" hreflang="pl" lang="pl" title="Lista największych przedsiębiorstw – Polish"><span>Polski</span></a></li><li class="interlanguage-link interwiki-pt mw-list-item"><a class="interlanguage-link-target" href="https://pt.wikipedia.org/wiki/Lista_das_maiores_empresas_do_mundo_por_receita" hreflang="pt" lang="pt" title="Lista das maiores empresas do mundo por receita – Portuguese"><span>Português</span></a></li><li class="interlanguage-link interwiki-ro mw-list-item"><a class="interlanguage-link-target" href="https://ro.wikipedia.org/wiki/List%C4%83_de_concerne-2005" hreflang="ro" lang="ro" title="Listă de concerne-2005 – Romanian"><span>Română</span></a></li><li class="interlanguage-link interwiki-fi mw-list-item"><a class="interlanguage-link-target" href="https://fi.wikipedia.org/wiki/Luettelo_maailman_suurimmista_yrityksist%C3%A4_liikevaihdon_mukaan" hreflang="fi" lang="fi" title="Luettelo maailman suurimmista yrityksistä liikevaihdon mukaan – Finnish"><span>Suomi</span></a></li><li class="interlanguage-link interwiki-ta mw-list-item"><a class="interlanguage-link-target" href="https://ta.wikipedia.org/wiki/%E0%AE%B5%E0%AE%B0%E0%AF%81%E0%AE%B5%E0%AE%BE%E0%AE%AF%E0%AF%8D_%E0%AE%85%E0%AE%9F%E0%AE%BF%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%9F%E0%AF%88%E0%AE%AF%E0%AE%BF%E0%AE%B2%E0%AF%8D_%E0%AE%AE%E0%AE%BF%E0%AE%95%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AF%86%E0%AE%B0%E0%AE%BF%E0%AE%AF_%E0%AE%A8%E0%AE%BF%E0%AE%B1%E0%AF%81%E0%AE%B5%E0%AE%A9%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%BF%E0%AE%A9%E0%AF%8D_%E0%AE%AA%E0%AE%9F%E0%AF%8D%E0%AE%9F%E0%AE%BF%E0%AE%AF%E0%AE%B2%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AF%8D" hreflang="ta" lang="ta" title="வருவாய் அடிப்படையில் மிகப்பெரிய நிறுவனங்களின் பட்டியல்கள் – Tamil"><span>தமிழ்</span></a></li><li class="interlanguage-link interwiki-tr mw-list-item"><a class="interlanguage-link-target" href="https://tr.wikipedia.org/wiki/Gelirlerine_g%C3%B6re_en_b%C3%BCy%C3%BCk_%C5%9Firketler_listesi" hreflang="tr" lang="tr" title="Gelirlerine göre en büyük şirketler listesi – Turkish"><span>Türkçe</span></a></li><li class="interlanguage-link interwiki-ur mw-list-item"><a class="interlanguage-link-target" href="https://ur.wikipedia.org/wiki/%D8%A8%DA%91%DB%8C_%DA%A9%D9%85%D9%BE%D9%86%D9%8A%D9%88%DA%BA_%DA%A9%DB%8C_%D9%81%DB%81%D8%B1%D8%B3%D8%AA_%D8%A8%D9%84%D8%AD%D8%A7%D8%B8_%D8%A2%D9%85%D8%AF%D9%86%DB%8C" hreflang="ur" lang="ur" title="بڑی کمپنيوں کی فہرست بلحاظ آمدنی – Urdu"><span>اردو</span></a></li><li class="interlanguage-link interwiki-vi mw-list-item"><a class="interlanguage-link-target" href="https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_c%C3%B4ng_ty_l%E1%BB%9Bn_nh%E1%BA%A5t_th%E1%BA%BF_gi%E1%BB%9Bi_theo_doanh_thu" hreflang="vi" lang="vi" title="Danh sách công ty lớn nhất thế giới theo doanh thu – Vietnamese"><span>Tiếng Việt</span></a></li>
</ul>
<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a class="wbc-editpage" href="https://www.wikidata.org/wiki/Special:EntityPage/Q900297#sitelinks-wikipedia" title="Edit interlanguage links">Edit links</a></span></div>
</div>
</div>
</div>
</header>
<div class="vector-page-toolbar">
<div class="vector-page-toolbar-container">
<div id="left-navigation">
<nav aria-label="Namespaces">
<div class="vector-menu vector-menu-tabs mw-portlet mw-portlet-associated-pages" id="p-associated-pages">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="selected vector-tab-noicon mw-list-item" id="ca-nstab-main"><a accesskey="c" href="/wiki/List_of_largest_companies_by_revenue" title="View the content page [c]"><span>Article</span></a></li><li class="vector-tab-noicon mw-list-item" id="ca-talk"><a accesskey="t" href="/wiki/Talk:List_of_largest_companies_by_revenue" rel="discussion" title="Discuss improvements to the content page [t]"><span>Talk</span></a></li>
</ul>
</div>
</div>
<div class="vector-dropdown emptyPortlet" id="vector-variants-dropdown">
<input aria-haspopup="true" aria-label="Change language variant" class="vector-dropdown-checkbox" data-event-name="ui.dropdown-vector-variants-dropdown" id="vector-variants-dropdown-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" for="vector-variants-dropdown-checkbox" id="vector-variants-dropdown-label"><span class="vector-dropdown-label-text">English</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-menu mw-portlet mw-portlet-variants emptyPortlet" id="p-variants">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
</ul>
</div>
</div>
</div>
</div>
</nav>
</div>
<div class="vector-collapsible" id="right-navigation">
<nav aria-label="Views">
<div class="vector-menu vector-menu-tabs mw-portlet mw-portlet-views" id="p-views">
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="selected vector-tab-noicon mw-list-item" id="ca-view"><a href="/wiki/List_of_largest_companies_by_revenue"><span>Read</span></a></li><li class="vector-tab-noicon mw-list-item" id="ca-edit"><a accesskey="e" href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit" title="Edit this page [e]"><span>Edit</span></a></li><li class="vector-tab-noicon mw-list-item" id="ca-history"><a accesskey="h" href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=history" title="Past revisions of this page [h]"><span>View history</span></a></li>
</ul>
</div>
</div>
</nav>
<nav aria-label="Page tools" class="vector-page-tools-landmark">
<div class="vector-dropdown vector-page-tools-dropdown" id="vector-page-tools-dropdown">
<input aria-haspopup="true" aria-label="Tools" class="vector-dropdown-checkbox" data-event-name="ui.dropdown-vector-page-tools-dropdown" id="vector-page-tools-dropdown-checkbox" role="button" type="checkbox"/>
<label aria-hidden="true" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" for="vector-page-tools-dropdown-checkbox" id="vector-page-tools-dropdown-label"><span class="vector-dropdown-label-text">Tools</span>
</label>
<div class="vector-dropdown-content">
<div class="vector-unpinned-container" id="vector-page-tools-unpinned-container">
<div class="vector-page-tools vector-pinnable-element" id="vector-page-tools">
<div class="vector-pinnable-header vector-page-tools-pinnable-header vector-pinnable-header-unpinned" data-feature-name="page-tools-pinned" data-pinnable-element-id="vector-page-tools" data-pinned-container-id="vector-page-tools-pinned-container" data-unpinned-container-id="vector-page-tools-unpinned-container">
<div class="vector-pinnable-header-label">Tools</div>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-page-tools.pin">move to sidebar</button>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-page-tools.unpin">hide</button>
</div>
<div class="vector-menu mw-portlet mw-portlet-cactions emptyPortlet vector-has-collapsible-items" id="p-cactions" title="More options">
<div class="vector-menu-heading">
		Actions
	</div>
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="selected vector-more-collapsible-item mw-list-item" id="ca-more-view"><a href="/wiki/List_of_largest_companies_by_revenue"><span>Read</span></a></li><li class="vector-more-collapsible-item mw-list-item" id="ca-more-edit"><a accesskey="e" href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit" title="Edit this page [e]"><span>Edit</span></a></li><li class="vector-more-collapsible-item mw-list-item" id="ca-more-history"><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=history"><span>View history</span></a></li>
</ul>
</div>
</div>
<div class="vector-menu mw-portlet mw-portlet-tb" id="p-tb">
<div class="vector-menu-heading">
		General
	</div>
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="mw-list-item" id="t-whatlinkshere"><a accesskey="j" href="/wiki/Special:WhatLinksHere/List_of_largest_companies_by_revenue" title="List of all English Wikipedia pages containing links to this page [j]"><span>What links here</span></a></li><li class="mw-list-item" id="t-recentchangeslinked"><a accesskey="k" href="/wiki/Special:RecentChangesLinked/List_of_largest_companies_by_revenue" rel="nofollow" title="Recent changes in pages linked from this page [k]"><span>Related changes</span></a></li><li class="mw-list-item" id="t-upload"><a accesskey="u" href="/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]"><span>Upload file</span></a></li><li class="mw-list-item" id="t-specialpages"><a accesskey="q" href="/wiki/Special:SpecialPages" title="A list of all special pages [q]"><span>Special pages</span></a></li><li class="mw-list-item" id="t-permalink"><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;oldid=1225623550" title="Permanent link to this revision of this page"><span>Permanent link</span></a></li><li class="mw-list-item" id="t-info"><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=info" title="More information about this page"><span>Page information</span></a></li><li class="mw-list-item" id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=List_of_largest_companies_by_revenue&amp;id=1225623550&amp;wpFormIdentifier=titleform" title="Information on how to cite this page"><span>Cite this page</span></a></li><li class="mw-list-item" id="t-urlshortener"><a href="/w/index.php?title=Special:UrlShortener&amp;url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FList_of_largest_companies_by_revenue"><span>Get shortened URL</span></a></li><li class="mw-list-item" id="t-urlshortener-qrcode"><a href="/w/index.php?title=Special:QrCode&amp;url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FList_of_largest_companies_by_revenue"><span>Download QR code</span></a></li><li class="mw-list-item" id="t-wikibase"><a accesskey="g" href="https://www.wikidata.org/wiki/Special:EntityPage/Q900297" title="Structured data on this page hosted by Wikidata [g]"><span>Wikidata item</span></a></li>
</ul>
</div>
</div>
<div class="vector-menu mw-portlet mw-portlet-coll-print_export" id="p-coll-print_export">
<div class="vector-menu-heading">
		Print/export
	</div>
<div class="vector-menu-content">
<ul class="vector-menu-content-list">
<li class="mw-list-item" id="coll-download-as-rl"><a href="/w/index.php?title=Special:DownloadAsPdf&amp;page=List_of_largest_companies_by_revenue&amp;action=show-download-screen" title="Download this page as a PDF file"><span>Download as PDF</span></a></li><li class="mw-list-item" id="t-print"><a accesskey="p" href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;printable=yes" title="Printable version of this page [p]"><span>Printable version</span></a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</nav>
</div>
</div>
</div>
<div class="vector-column-end">
<div class="vector-sticky-pinned-container">
<nav aria-label="Page tools" class="vector-page-tools-landmark">
<div class="vector-pinned-container" id="vector-page-tools-pinned-container">
</div>
</nav>
<nav aria-label="Appearance" class="vector-appearance-landmark">
<div class="vector-pinned-container" id="vector-appearance-pinned-container">
<div class="vector-appearance vector-pinnable-element" id="vector-appearance">
<div class="vector-pinnable-header vector-appearance-pinnable-header vector-pinnable-header-pinned" data-feature-name="appearance-pinned" data-pinnable-element-id="vector-appearance" data-pinned-container-id="vector-appearance-pinned-container" data-unpinned-container-id="vector-appearance-unpinned-container">
<div class="vector-pinnable-header-label">Appearance</div>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-appearance.pin">move to sidebar</button>
<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-appearance.unpin">hide</button>
</div>
</div>
</div>
</nav>
</div>
</div>
<div aria-labelledby="firstHeading" class="vector-body" data-mw-ve-target-container="" id="bodyContent">
<div class="vector-body-before-content">
<div class="mw-indicators">
</div>
<div class="noprint" id="siteSub">From Wikipedia, the free encyclopedia</div>
</div>
<div id="contentSub"><div id="mw-content-subtitle"></div></div>
<div class="mw-body-content" id="mw-content-text"><div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"><p class="mw-empty-elt">
</p>
<figure class="mw-halign-right" typeof="mw:File/Thumb"><a class="mw-file-description" href="/wiki/File:Walmart_store_exterior_5266815680.jpg"><img class="mw-file-element" data-file-height="1298" data-file-width="1728" decoding="async" height="183" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/243px-Walmart_store_exterior_5266815680.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/365px-Walmart_store_exterior_5266815680.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/486px-Walmart_store_exterior_5266815680.jpg 2x" width="243"/></a><figcaption><a href="/wiki/Walmart" title="Walmart">Walmart</a> has been the world's largest company by revenue since 2014.<sup class="reference" id="cite_ref-W_1-0"><a href="#cite_note-W-1">[1]</a></sup></figcaption></figure>
<p>This list comprises the world's largest companies by <b><a href="/wiki/Consolidation_(business)" title="Consolidation (business)">consolidated</a> <a href="/wiki/Revenue" title="Revenue">revenue</a></b>, according to the <a href="/wiki/Fortune_Global_500" title="Fortune Global 500"><i>Fortune</i> Global 500</a> 2023 rankings and other sources.<sup class="reference" id="cite_ref-Fortune_500_2-0"><a href="#cite_note-Fortune_500-2">[2]</a></sup> American retail corporation <a href="/wiki/Walmart" title="Walmart">Walmart</a> has been the world's largest company by revenue since 2014.<sup class="reference" id="cite_ref-W_1-1"><a href="#cite_note-W-1">[1]</a></sup>
</p><p>The list is limited to the largest 50 companies, all of which have annual revenues exceeding US$130 billion. This list is incomplete, as not all companies disclose their information to the media and/or general public.<sup class="reference" id="cite_ref-3"><a href="#cite_note-3">[3]</a></sup>
</p><p>Out of 50 largest companies 20 are <a href="/wiki/United_States" title="United States">American</a>, 19 <a href="/wiki/Asia" title="Asia">Asian</a> and 11 <a href="/wiki/Europe" title="Europe">European</a>.<sup class="reference" id="cite_ref-Fortune_500_2-1"><a href="#cite_note-Fortune_500-2">[2]</a></sup>
</p>
<meta property="mw:PageProp/toc">
<h2><span class="mw-headline" id="List">List</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit&amp;section=1" title="Edit section: List"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Information in the list relates to the most recent <a href="/wiki/Fiscal_year" title="Fiscal year">fiscal year</a> (mostly FY 2022 or 2023).
</p>
<style data-mw-deduplicate="TemplateStyles:r1224903325">@media screen{.mw-parser-output .sticky-header>thead>tr:first-child,.mw-parser-output .sticky-header>caption+tbody>tr:first-child,.mw-parser-output .sticky-header>tbody:first-child>tr:first-child,.mw-parser-output .sticky-header-multi>thead{position:sticky;top:0;z-index:10}.mw-parser-output .sticky-header:not(.wikitable),.mw-parser-output .sticky-header-multi:not(.wikitable),body.skin-minerva .mw-parser-output .sticky-header-multi.wikitable{background-color:white}html.skin-theme-clientpref-night body.skin-minerva .mw-parser-output .sticky-header-multi.wikitable{background-color:#101418}@media(prefers-color-scheme:dark){html.skin-theme-clientpref-os body.skin-minerva .mw-parser-output .sticky-header-multi.wikitable{background-color:#101418}}.mw-parser-output .sticky-header-multi>thead,.mw-parser-output .sticky-header:not(.wikitable)>thead,.mw-parser-output .sticky-header:not(.wikitable)>tbody,.mw-parser-output .sticky-header:not(.wikitable)>thead>tr,.mw-parser-output .sticky-header:not(.wikitable)>tbody>tr{background-color:inherit}.mw-parser-output .sticky-header.wikitable,.mw-parser-output .sticky-header-multi.wikitable{border-collapse:separate;border-spacing:0;border-width:0 1px 1px 0}.mw-parser-output .sticky-header.wikitable td,.mw-parser-output .sticky-header.wikitable th,.mw-parser-output .sticky-header-multi.wikitable td,.mw-parser-output .sticky-header-multi.wikitable th{border-width:1px 0 0 1px}body.skin-timeless .mw-parser-output .sticky-header.wikitable,body.skin-timeless .mw-parser-output .sticky-header-multi.wikitable{border-bottom-width:0.2em;padding:0}.mw-parser-output .sticky-header.static-row-numbers.wikitable tr::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable tr::before{border-left-width:1px}.mw-parser-output .sticky-header.static-row-numbers.wikitable>thead>tr:first-child::before,.mw-parser-output .sticky-header.static-row-numbers.wikitable>caption+tbody>tr:first-child::before,.mw-parser-output .sticky-header.static-row-numbers.wikitable>tbody:first-child>tr:first-child::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable>thead>tr:first-child::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable>caption+tbody>tr:first-child::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable>tbody:first-child>tr:first-child::before,.mw-parser-output .sticky-header.static-row-numbers.wikitable .sortbottom::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable .sortbottom::before{border-top-width:1px}.mw-parser-output .sticky-header.static-row-numbers.wikitable .sortbottom~.sortbottom::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable .sortbottom~.sortbottom::before{border-top-width:0}.mw-parser-output .sticky-header.static-row-numbers.wikitable>tbody>tr:not(.static-row-header)::before,.mw-parser-output .sticky-header-multi.static-row-numbers.wikitable>tbody>tr:not(.static-row-header)::before{border-bottom-width:0!important;border-right-width:0!important}body.skin-timeless .mw-parser-output .content-table-scrollbar,body.skin-timeless .mw-parser-output .overflowed,body.skin-timeless .mw-parser-output .overflowed .content-table{overflow:visible}body.skin-timeless .mw-parser-output .scroll-right.overflowed .content-table-right{box-shadow:none;border-left:none}.mw-parser-output .sticky-header-scroll{margin-bottom:1em;margin-top:1em;max-height:75vh;max-width:max-content;min-width:300px;overflow-y:auto}.mw-parser-output .sticky-header-scroll .sticky-header,.mw-parser-output .sticky-header-scroll .sticky-header-multi{margin-bottom:0;margin-top:0}.mw-parser-output .sticky-header-scroll .sticky-header caption,.mw-parser-output .sticky-header-scroll .sticky-header-multi caption{text-align:left}}@media screen and (min-width:1000px){body.vector-sticky-header-visible .mw-parser-output .sticky-header>thead>tr:first-child,body.vector-sticky-header-visible .mw-parser-output .sticky-header>caption+tbody>tr:first-child,body.vector-sticky-header-visible .mw-parser-output .sticky-header>tbody:first-child>tr:first-child,body.vector-sticky-header-visible .mw-parser-output .sticky-header-multi>thead{top:3.125rem}body.vector-sticky-header-visible .mw-parser-output .sticky-header-scroll .sticky-header>thead>tr:first-child,body.vector-sticky-header-visible .mw-parser-output .sticky-header-scroll .sticky-header>caption+tbody>tr:first-child,body.vector-sticky-header-visible .mw-parser-output .sticky-header-scroll .sticky-header>tbody:first-child>tr:first-child,body.vector-sticky-header-visible .mw-parser-output .sticky-header-scroll .sticky-header-multi>thead{top:0}}@media screen and (min-width:851px){body.skin-timeless .mw-parser-output .sticky-header>thead>tr:first-child,body.skin-timeless .mw-parser-output .sticky-header>caption+tbody>tr:first-child,body.skin-timeless .mw-parser-output .sticky-header>tbody:first-child>tr:first-child,body.skin-timeless .mw-parser-output .sticky-header-multi>thead{top:3.51em}body.skin-timeless .mw-parser-output .sticky-header-scroll .sticky-header>thead>tr:first-child,body.skin-timeless .mw-parser-output .sticky-header-scroll .sticky-header>caption+tbody>tr:first-child,body.skin-timeless .mw-parser-output .sticky-header-scroll .sticky-header>tbody:first-child>tr:first-child,body.skin-timeless .mw-parser-output .sticky-header-scroll .sticky-header-multi>thead{top:0}}@media screen and (max-width:720px){body.skin-minerva .mw-parser-output .sticky-header,body.skin-minerva .mw-parser-output .sticky-header-multi{display:table}body.skin-minerva .mw-parser-output .sticky-header>caption,body.skin-minerva .mw-parser-output .sticky-header-multi>caption{display:table-caption}}</style><style data-mw-deduplicate="TemplateStyles:r1212405398">@media screen{html.client-js .mw-parser-output .sort-under.sortable.wikitable th.headerSort,html.client-js .mw-parser-output .sort-under-right.sortable.wikitable th.headerSort,html.client-js .mw-parser-output .sort-under-center.sortable.wikitable th.headerSort{padding-right:0.4em}html.client-js .mw-parser-output .sort-under.sortable:not(.wikitable) th.headerSort,html.client-js .mw-parser-output .sort-under-right.sortable:not(.wikitable) th.headerSort,html.client-js .mw-parser-output .sort-under-center.sortable:not(.wikitable) th.headerSort{padding-right:1px}html.client-js body.skin-minerva .mw-parser-output .sort-under.sortable.wikitable th.headerSort,html.client-js body.skin-minerva .mw-parser-output .sort-under-right.sortable.wikitable th.headerSort,html.client-js body.skin-minerva .mw-parser-output .sort-under-center.sortable.wikitable th.headerSort{padding-right:0.2em}html.client-js body.skin-timeless .mw-parser-output .sort-under.sortable.wikitable th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under-right.sortable.wikitable th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under-center.sortable.wikitable th.headerSort{padding-right:0.5em}html.client-js .mw-parser-output .sort-under-center.sortable th.headerSort{background-position:center bottom 0.2em}html.client-js .mw-parser-output .sort-under.sortable th.headerSort,html.client-js .mw-parser-output .sort-under-right.sortable th.headerSort{background-position:right bottom 0.2em}html.client-js .mw-parser-output .sort-under.sortable th.headerSort,html.client-js .mw-parser-output .sort-under.sortable th.unsortable,html.client-js .mw-parser-output .sort-under-right.sortable th.headerSort,html.client-js .mw-parser-output .sort-under-right.sortable th.unsortable,html.client-js .mw-parser-output .sort-under-center.sortable th.headerSort,html.client-js .mw-parser-output .sort-under-center.sortable th.unsortable{padding-bottom:1em}html.client-js body.skin-timeless .mw-parser-output .sort-under.sortable.wikitable th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under.sortable.wikitable th.unsortable,html.client-js body.skin-timeless .mw-parser-output .sort-under-right.sortable.wikitable th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under-right.sortable.wikitable th.unsortable,html.client-js body.skin-timeless .mw-parser-output .sort-under-center.sortable.wikitable th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under-center.sortable.wikitable th.unsortable{padding-bottom:1.2em}html.client-js body.skin-timeless .mw-parser-output .sort-under.sortable:not(.wikitable) th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under.sortable:not(.wikitable) th.unsortable,html.client-js body.skin-timeless .mw-parser-output .sort-under-right.sortable:not(.wikitable) th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under-right.sortable:not(.wikitable) th.unsortable,html.client-js body.skin-timeless .mw-parser-output .sort-under-center.sortable:not(.wikitable) th.headerSort,html.client-js body.skin-timeless .mw-parser-output .sort-under-center.sortable:not(.wikitable) th.unsortable,html.client-js body.skin-minerva .mw-parser-output .sort-under.sortable:not(.wikitable) th.headerSort,html.client-js body.skin-minerva .mw-parser-output .sort-under.sortable:not(.wikitable) th.unsortable,html.client-js body.skin-minerva .mw-parser-output .sort-under-right.sortable:not(.wikitable) th.headerSort,html.client-js body.skin-minerva .mw-parser-output .sort-under-right.sortable:not(.wikitable) th.unsortable,html.client-js body.skin-minerva .mw-parser-output .sort-under-center.sortable:not(.wikitable) th.headerSort,html.client-js body.skin-minerva .mw-parser-output .sort-under-center.sortable:not(.wikitable) th.unsortable{padding-bottom:0.8em}html.client-js .mw-parser-output .static-row-numbers.sort-under.sortable thead tr:only-child::before,html.client-js .mw-parser-output .static-row-numbers.sort-under-right.sortable thead tr:only-child::before,html.client-js .mw-parser-output .static-row-numbers.sort-under-center.sortable thead tr:only-child::before{padding-bottom:0.9em}html.client-js body.skin-timeless .mw-parser-output .static-row-numbers.sort-under.sortable thead tr:only-child::before,html.client-js body.skin-timeless .mw-parser-output .static-row-numbers.sort-under-right.sortable thead tr:only-child::before,html.client-js body.skin-timeless .mw-parser-output .static-row-numbers.sort-under-center.sortable thead tr:only-child::before,html.client-js body.skin-minerva .mw-parser-output .static-row-numbers.sort-under.sortable thead tr:only-child::before,html.client-js body.skin-minerva .mw-parser-output .static-row-numbers.sort-under-right.sortable thead tr:only-child::before,html.client-js body.skin-minerva .mw-parser-output .static-row-numbers.sort-under-center.sortable thead tr:only-child::before{padding-bottom:0.8em}}</style>
<table class="wikitable sortable sticky-header-multi sort-under" style="text-align:left;">
<tbody><tr>
<th rowspan="2" scope="col">Rank
</th>
<th rowspan="2" scope="col">Name
</th>
<th rowspan="2" scope="col">Industry
</th>
<th scope="col">Revenue
</th>
<th scope="col">Profit
</th>
<th rowspan="2" scope="col">Employees
</th>
<th rowspan="2" scope="col">Headquarters<sup class="reference" id="cite_ref-4"><a href="#cite_note-4">[note 1]</a></sup>
</th>
<th rowspan="2" scope="col"><a href="/wiki/State-owned_enterprise" title="State-owned enterprise">State-owned</a>
</th>
<th class="unsortable" rowspan="2" scope="col"><abbr title="Reference(s)">Ref.</abbr>
</th>
<th rowspan="2" scope="col">Revenue per worker
</th></tr>
<tr>
<th colspan="2" scope="col"><small>USD millions</small>
</th></tr>
<tr>
<th scope="col">1
</th>
<td><a href="/wiki/Walmart" title="Walmart">Walmart</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $611,289</td>
<td style="text-align:left;">$11,680</td>
<td style="text-align:right;">2,100,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-W_1-2"><a href="#cite_note-W-1">[1]</a></sup>
</td>
<td>$291,090.00
</td></tr>
<tr>
<th scope="row">2
</th>
<td><a href="/wiki/Saudi_Aramco" title="Saudi Aramco">Saudi Aramco</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $603,651</td>
<td style="text-align:left;">$159,069</td>
<td style="text-align:right;">70,496</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Saudi_Arabia" title="Saudi Arabia"><img alt="Saudi Arabia" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></a></span></span> Saudi Arabia</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-5"><a href="#cite_note-5">[4]</a></sup>
</td>
<td>$8,562,911.37
</td></tr>
<tr>
<th scope="row">3
</th>
<td><a href="/wiki/Amazon_(company)" title="Amazon (company)">Amazon</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $574,785</td>
<td style="text-align:left;">$30,425</td>
<td style="text-align:right;">1,525,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-6"><a href="#cite_note-6">[5]</a></sup>
</td>
<td>$376,908.20
</td></tr>
<tr>
<th scope="row">4
</th>
<td><a href="/wiki/State_Grid_Corporation_of_China" title="State Grid Corporation of China">State Grid Corporation of China</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $530,009</td>
<td style="text-align:left;">$8,192</td>
<td style="text-align:right;">870,287
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-7"><a href="#cite_note-7">[6]</a></sup>
</td>
<td>$609,004.85
</td></tr>
<tr>
<th scope="row">5
</th>
<td><a href="/wiki/Vitol" title="Vitol">Vitol</a>
</td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $505,000
</td>
<td>$15,000
</td>
<td style="text-align:right;">1,560
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/15px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/23px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/30px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="15"/></span></span> </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a>
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-8"><a href="#cite_note-8">[7]</a></sup><sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[8]</a></sup>
</td>
<td>$323,717,948.72
</td></tr>
<tr>
<th scope="row">6
</th>
<td><a href="/wiki/China_National_Petroleum_Corporation" title="China National Petroleum Corporation">China National Petroleum Corporation</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $483,019</td>
<td style="text-align:left;">$21,080</td>
<td style="text-align:right;">1,087,049</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-10"><a href="#cite_note-10">[9]</a></sup>
</td>
<td>$444,339.68
</td></tr>
<tr>
<th scope="row">7
</th>
<td><a href="/wiki/China_Petrochemical_Corporation" title="China Petrochemical Corporation">China Petrochemical Corporation</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $471,154</td>
<td style="text-align:left;">$9,657</td>
<td style="text-align:right;">527,487</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[10]</a></sup>
</td>
<td>$893,204.95
</td></tr>
<tr>
<th scope="row">8
</th>
<td><a href="/wiki/ExxonMobil" title="ExxonMobil">ExxonMobil</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $413,680</td>
<td style="text-align:left;">$55,740</td>
<td style="text-align:right;">63,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:0_12-0"><a href="#cite_note-:0-12">[11]</a></sup>
</td>
<td>$6,566,349.21
</td></tr>
<tr>
<th scope="row">9
</th>
<td><a href="/wiki/Apple_Inc." title="Apple Inc.">Apple</a></td>
<td><a href="/wiki/Electronics_industry" title="Electronics industry">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $394,328</td>
<td style="text-align:left;">$99,803</td>
<td style="text-align:right;">164,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-13"><a href="#cite_note-13">[12]</a></sup>
</td>
<td>$2,404,439.02
</td></tr>
<tr>
<th scope="row">10
</th>
<td><a href="/wiki/Shell_plc" title="Shell plc">Shell</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $386,201</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">93,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-14"><a href="#cite_note-14">[13]</a></sup>
</td>
<td>$4,152,698.92
</td></tr>
<tr>
<th scope="row">11
</th>
<td><a href="/wiki/UnitedHealth_Group" title="UnitedHealth Group">UnitedHealth Group</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $324,162</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">400,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-15"><a href="#cite_note-15">[14]</a></sup>
</td>
<td>$810,405.00
</td></tr>
<tr>
<th scope="row">12
</th>
<td><a href="/wiki/CVS_Health" title="CVS Health">CVS Health</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $322,467</td>
<td style="text-align:left;">$4,149</td>
<td style="text-align:right;">259,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-16"><a href="#cite_note-16">[15]</a></sup>
</td>
<td>$1,242,647.40
</td></tr>
<tr>
<th scope="row">13
</th>
<td><a href="/wiki/Trafigura" title="Trafigura">Trafigura</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $318,476</td>
<td style="text-align:left;">$6,994</td>
<td style="text-align:right;">12,347</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Singapore" title="Singapore"><img alt="Singapore" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></a></span></span> Singapore</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-17"><a href="#cite_note-17">[16]</a></sup>
</td>
<td>$25,793,796.06
</td></tr>
<tr>
<th scope="row">14
</th>
<td><a href="/wiki/China_State_Construction_Engineering" title="China State Construction Engineering">China State Construction Engineering</a></td>
<td><a href="/wiki/Construction" title="Construction">Construction</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $305,885</td>
<td style="text-align:left;">$4,234</td>
<td style="text-align:right;">382,492</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-18"><a href="#cite_note-18">[17]</a></sup>
</td>
<td>$799,716.07
</td></tr>
<tr>
<th scope="row">15
</th>
<td><a href="/wiki/Berkshire_Hathaway" title="Berkshire Hathaway">Berkshire Hathaway</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $302,089</td>
<td style="text-align:left;">−$22,819</td>
<td style="text-align:right;">383,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-19"><a href="#cite_note-19">[18]</a></sup>
</td>
<td>$788,744.13
</td></tr>
<tr>
<th scope="row">16
</th>
<td><a href="/wiki/Volkswagen_Group" title="Volkswagen Group">Volkswagen Group</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $293,685</td>
<td style="text-align:left;">$15,233</td>
<td style="text-align:right;">675,805</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-20"><a href="#cite_note-20">[19]</a></sup>
</td>
<td>$434,570.62
</td></tr>
<tr>
<th scope="row">17
</th>
<td><a href="/wiki/Uniper" title="Uniper">Uniper</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $288,309</td>
<td style="text-align:left;">−$19,961</td>
<td style="text-align:right;">7,008</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-21"><a href="#cite_note-21">[20]</a></sup>
</td>
<td>$41,139,982.88
</td></tr>
<tr>
<th scope="row">18
</th>
<td><a href="/wiki/Alphabet_Inc." title="Alphabet Inc.">Alphabet</a></td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $282,836</td>
<td style="text-align:left;">$59,972</td>
<td style="text-align:right;">190,234</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-22"><a href="#cite_note-22">[21]</a></sup>
</td>
<td>$1,486,779.44
</td></tr>
<tr>
<th scope="row">19
</th>
<td><a href="/wiki/McKesson_Corporation" title="McKesson Corporation">McKesson</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $276,711</td>
<td style="text-align:left;">$3,560</td>
<td style="text-align:right;">48,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-23"><a href="#cite_note-23">[22]</a></sup>
</td>
<td>$5,764,812.50
</td></tr>
<tr>
<th scope="row">20
</th>
<td><a href="/wiki/Toyota" title="Toyota">Toyota</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $274,491</td>
<td style="text-align:left;">$18,110</td>
<td style="text-align:right;">375,235</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-24"><a href="#cite_note-24">[23]</a></sup>
</td>
<td>$731,517.58
</td></tr>
<tr>
<th scope="row">21
</th>
<td><a href="/wiki/TotalEnergies" title="TotalEnergies">TotalEnergies</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $263,310</td>
<td style="text-align:left;">$20,526</td>
<td style="text-align:right;">101,279
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/France" title="France"><img alt="France" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></a></span></span> France
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-25"><a href="#cite_note-25">[24]</a></sup>
</td>
<td>$2,599,847.94
</td></tr>
<tr>
<th scope="row">22
</th>
<td><a href="/wiki/Glencore" title="Glencore">Glencore</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $255,984</td>
<td style="text-align:left;">$17,320</td>
<td style="text-align:right;">81,284</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Switzerland" title="Switzerland"><img alt="Switzerland" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></a></span></span> Switzerland</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-26"><a href="#cite_note-26">[25]</a></sup>
</td>
<td>$3,149,254.47
</td></tr>
<tr>
<th scope="row">23
</th>
<td><a href="/wiki/BP" title="BP">BP</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $248,891</td>
<td style="text-align:left;">−$2,487</td>
<td style="text-align:right;">67,600</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-27"><a href="#cite_note-27">[26]</a></sup>
</td>
<td>$3,681,819.53
</td></tr>
<tr>
<th scope="row">24
</th>
<td><a href="/wiki/Chevron_Corporation" title="Chevron Corporation">Chevron</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $246,252</td>
<td style="text-align:left;">$35,465</td>
<td style="text-align:right;">43,846</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-28"><a href="#cite_note-28">[27]</a></sup>
</td>
<td>$5,616,293.39
</td></tr>
<tr>
<th scope="row">25
</th>
<td><a href="/wiki/Cencora" title="Cencora">Cencora</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $238,587</td>
<td style="text-align:left;">$1,699</td>
<td style="text-align:right;">41,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-29"><a href="#cite_note-29">[28]</a></sup>
</td>
<td>$5,749,084.34
</td></tr>
<tr>
<th scope="row">26
</th>
<td><a href="/wiki/Samsung_Electronics" title="Samsung Electronics">Samsung Electronics</a>
</td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $234,129</td>
<td style="text-align:left;">$42,398</td>
<td style="text-align:right;">270,372</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/South_Korea" title="South Korea"><img alt="South Korea" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></a></span></span> South Korea</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-30"><a href="#cite_note-30">[29]</a></sup>
</td>
<td>$865,951.36
</td></tr>
<tr>
<th scope="row">27
</th>
<td><a href="/wiki/Costco" title="Costco">Costco</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $226,954</td>
<td style="text-align:left;">$5,844</td>
<td style="text-align:right;">304,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-31"><a href="#cite_note-31">[30]</a></sup>
</td>
<td>$746,559.21
</td></tr>
<tr>
<th scope="row">28
</th>
<td><a href="/wiki/Foxconn" title="Foxconn">Foxconn</a></td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $222,535</td>
<td style="text-align:left;">$4,751</td>
<td style="text-align:right;">767,062</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Taiwan" title="Taiwan"><img alt="Taiwan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></a></span></span> Taiwan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-32"><a href="#cite_note-32">[31]</a></sup>
</td>
<td>$290,113.45
</td></tr>
<tr>
<th scope="row">29
</th>
<td><a href="/wiki/Industrial_and_Commercial_Bank_of_China" title="Industrial and Commercial Bank of China">Industrial and Commercial Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $214,766</td>
<td style="text-align:left;">$53,589</td>
<td style="text-align:right;">427,587</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-33"><a href="#cite_note-33">[32]</a></sup>
</td>
<td>$502,274.39
</td></tr>
<tr>
<th scope="row">30
</th>
<td><a href="/wiki/Microsoft" title="Microsoft">Microsoft</a>
</td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $211,915
</td>
<td>$73,307
</td>
<td style="text-align:right;">221,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-34"><a href="#cite_note-34">[33]</a></sup>
</td>
<td>$897,149.32
</td></tr>
<tr>
<th scope="row">31
</th>
<td><a href="/wiki/China_Construction_Bank" title="China Construction Bank">China Construction Bank</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $202,753</td>
<td style="text-align:left;">$48,145</td>
<td style="text-align:right;">376,682</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-35"><a href="#cite_note-35">[34]</a></sup>
</td>
<td>$538,260.39
</td></tr>
<tr>
<th>32
</th>
<td><a href="/wiki/Stellantis" title="Stellantis">Stellantis</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $188,888
</td>
<td>$17,669
</td>
<td style="text-align:right">272,367
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Netherlands" title="Netherlands"><img alt="Netherlands" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></a></span></span> Netherlands
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-36"><a href="#cite_note-36">[35]</a></sup>
</td>
<td>$693,505.45
</td></tr>
<tr>
<th scope="row">33
</th>
<td><a href="/wiki/Agricultural_Bank_of_China" title="Agricultural Bank of China">Agricultural Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $187,061</td>
<td style="text-align:left;">$38,524</td>
<td style="text-align:right;">452,258</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-37"><a href="#cite_note-37">[36]</a></sup>
</td>
<td>$413,615.68
</td></tr>
<tr>
<th scope="row">34
</th>
<td><a href="/wiki/Ping_An_Insurance" title="Ping An Insurance">Ping An Insurance</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $181,566</td>
<td style="text-align:left;">$12,454</td>
<td style="text-align:right;">344,223</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-38"><a href="#cite_note-38">[37]</a></sup>
</td>
<td>$527,466.21
</td></tr>
<tr>
<th scope="row">35
</th>
<td><a href="/wiki/Cardinal_Health" title="Cardinal Health">Cardinal Health</a></td>
<td><a href="/wiki/Health_care" title="Health care">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $181,364</td>
<td style="text-align:left;">−$933</td>
<td style="text-align:right;">46,035
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-39"><a href="#cite_note-39">[38]</a></sup>
</td>
<td>$3,939,698.06
</td></tr>
<tr>
<th>36
</th>
<td><a href="/wiki/Cigna" title="Cigna">Cigna</a>
</td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,516
</td>
<td>$6,668
</td>
<td style="text-align:right;">70,231
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-40"><a href="#cite_note-40">[39]</a></sup>
</td>
<td>$2,570,317.95
</td></tr>
<tr>
<th scope="row">37
</th>
<td><a href="/wiki/Marathon_Petroleum" title="Marathon Petroleum">Marathon Petroleum</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,012</td>
<td style="text-align:left;">$14,516</td>
<td style="text-align:right;">17,800</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-41"><a href="#cite_note-41">[40]</a></sup>
</td>
<td>$10,113,033.71
</td></tr>
<tr>
<th scope="row">38
</th>
<td><a href="/wiki/Phillips_66" title="Phillips 66">Phillips 66</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $175,702</td>
<td style="text-align:left;">$11,024</td>
<td style="text-align:right;">13,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-42"><a href="#cite_note-42">[41]</a></sup>
</td>
<td>$13,515,538.46
</td></tr>
<tr>
<th>39
</th>
<td><a href="/wiki/Sinochem" title="Sinochem">Sinochem</a>
</td>
<td><a href="/wiki/Chemical_industry" title="Chemical industry">Chemicals</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $173,834
</td>
<td>–$1
</td>
<td style="text-align:right">220,760
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-43"><a href="#cite_note-43">[42]</a></sup>
</td>
<td>$787,434.32
</td></tr>
<tr>
<th scope="row">40
</th>
<td><a href="/wiki/China_Railway_Engineering_Corporation" title="China Railway Engineering Corporation">China Railway Engineering Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,669
</td>
<td>$2,035
</td>
<td style="text-align:right;">314,792
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-44"><a href="#cite_note-44">[43]</a></sup>
</td>
<td>$545,341.05
</td></tr>
<tr>
<th scope="row">41
</th>
<td><a href="/wiki/Valero_Energy" title="Valero Energy">Valero Energy</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,189</td>
<td style="text-align:left;">$11,528</td>
<td style="text-align:right;">9,743</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:2_45-0"><a href="#cite_note-:2-45">[44]</a></sup>
</td>
<td>$17,570,460.84
</td></tr>
<tr>
<th scope="row">42
</th>
<td><a href="/wiki/Gazprom" title="Gazprom">Gazprom</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $167,832</td>
<td style="text-align:left;">$17,641</td>
<td style="text-align:right;">468,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a>
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-46"><a href="#cite_note-46">[45]</a></sup>
</td>
<td>$358,615.38
</td></tr>
<tr>
<th scope="row">43
</th>
<td><a href="/wiki/Cargill" title="Cargill">Cargill</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $165,000</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">155,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-47"><a href="#cite_note-47">[46]</a></sup>
</td>
<td>$1,064,516.13
</td></tr>
<tr>
<th scope="row">44
</th>
<td><a href="/wiki/China_National_Offshore_Oil_Corporation" title="China National Offshore Oil Corporation">China National Offshore Oil Corporation</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $164,762</td>
<td style="text-align:left;">$16,988</td>
<td style="text-align:right;">81,775</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-48"><a href="#cite_note-48">[47]</a></sup>
</td>
<td>$2,014,821.16
</td></tr>
<tr>
<th scope="row">45
</th>
<td><a href="/wiki/China_Railway_Construction_Corporation" title="China Railway Construction Corporation">China Railway Construction Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $163,037
</td>
<td>$1,800
</td>
<td style="text-align:right;">342,098
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-49"><a href="#cite_note-49">[48]</a></sup>
</td>
<td>$476,579.81
</td></tr>
<tr>
<th scope="row">46
</th>
<td><a href="/wiki/Baowu" title="Baowu">Baowu</a>
</td>
<td><a href="/wiki/Steel" title="Steel">Steel</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $161,698
</td>
<td>$2,493
</td>
<td style="text-align:right;">245,675
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-50"><a href="#cite_note-50">[49]</a></sup>
</td>
<td>$658,178.49
</td></tr>
<tr>
<th scope="row">47
</th>
<td><a href="/wiki/Schwarz_Gruppe" title="Schwarz Gruppe">Schwarz Gruppe</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,800</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">575,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-51"><a href="#cite_note-51">[50]</a></sup>
</td>
<td>$277,913.04
</td></tr>
<tr>
<th>48
</th>
<td><a class="mw-redirect" href="/wiki/Mitsubishi_Group" title="Mitsubishi Group">Mitsubishi Group</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,371
</td>
<td>$8,723
</td>
<td style="text-align:right">79,706
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-52"><a href="#cite_note-52">[51]</a></sup>
</td>
<td>$1,999,485.61
</td></tr>
<tr>
<th scope="row">49
</th>
<td><a href="/wiki/Ford_Motor_Company" title="Ford Motor Company">Ford Motor Company</a></td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $158,057</td>
<td style="text-align:left;">−$1,981</td>
<td style="text-align:right;">173,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-53"><a href="#cite_note-53">[52]</a></sup>
</td>
<td>$913,624.28
</td></tr>
<tr>
<th scope="row">50
</th>
<td><a href="/wiki/Mercedes-Benz_Group" title="Mercedes-Benz Group">Mercedes-Benz Group</a></td>
<td><a href="/wiki/Automotive_industry" title="Automotive industry">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $157,403</td>
<td style="text-align:left;">$15,252</td>
<td style="text-align:right;">168,797</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-54"><a href="#cite_note-54">[53]</a></sup>
</td>
<td>$932,498.80
</td></tr></tbody></table>
<h2><span class="mw-headline" id="By_country">By country</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit&amp;section=2" title="Edit section: By country"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table class="wikitable sortable plainrowheaders" style="text-align: center">
<caption>Breakdown by country
</caption>
<tbody><tr>
<th scope="col">Rank
</th>
<th scope="col">Country
</th>
<th scope="col">Companies
</th></tr>
<tr>
<th scope="row">1
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/United_States" title="United States">United States of America</a></td>
<td>20
</td></tr>
<tr>
<th scope="row">2
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/China" title="China">China</a></td>
<td>13
</td></tr>
<tr>
<th scope="row">3
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Germany" title="Germany">Germany</a></td>
<td>4
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></span></span>  </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Japan" title="Japan">Japan</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Netherlands" title="Netherlands">Netherlands</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/South_Korea" title="South Korea">South Korea</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/France" title="France">France</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Saudi_Arabia" title="Saudi Arabia">Saudi Arabia</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Singapore" title="Singapore">Singapore</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Taiwan" title="Taiwan">Taiwan</a></td>
<td>1
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Notes">Notes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit&amp;section=3" title="Edit section: Notes"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<style data-mw-deduplicate="TemplateStyles:r1217336898">.mw-parser-output .reflist{font-size:90%;margin-bottom:0.5em;list-style-type:decimal}.mw-parser-output .reflist .references{font-size:100%;margin-bottom:0;list-style-type:inherit}.mw-parser-output .reflist-columns-2{column-width:30em}.mw-parser-output .reflist-columns-3{column-width:25em}.mw-parser-output .reflist-columns{margin-top:0.3em}.mw-parser-output .reflist-columns ol{margin-top:0}.mw-parser-output .reflist-columns li{page-break-inside:avoid;break-inside:avoid-column}.mw-parser-output .reflist-upper-alpha{list-style-type:upper-alpha}.mw-parser-output .reflist-upper-roman{list-style-type:upper-roman}.mw-parser-output .reflist-lower-alpha{list-style-type:lower-alpha}.mw-parser-output .reflist-lower-greek{list-style-type:lower-greek}.mw-parser-output .reflist-lower-roman{list-style-type:lower-roman}</style><div class="reflist">
<div class="mw-references-wrap"><ol class="references">
<li id="cite_note-4"><span class="mw-cite-backlink"><b><a href="#cite_ref-4">^</a></b></span> <span class="reference-text">As reported by source.</span>
</li>
</ol></div></div>
<h2><span class="mw-headline" id="See_also">See also</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit&amp;section=4" title="Edit section: See also"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<style data-mw-deduplicate="TemplateStyles:r1214689105">.mw-parser-output .portalbox{padding:0;margin:0.5em 0;display:table;box-sizing:border-box;max-width:175px;list-style:none}.mw-parser-output .portalborder{border:solid #aaa 1px;padding:0.1em;background:#f9f9f9}.mw-parser-output .portalbox-entry{display:table-row;font-size:85%;line-height:110%;height:1.9em;font-style:italic;font-weight:bold}.mw-parser-output .portalbox-image{display:table-cell;padding:0.2em;vertical-align:middle;text-align:center}.mw-parser-output .portalbox-link{display:table-cell;padding:0.2em 0.2em 0.2em 0.3em;vertical-align:middle}@media(min-width:720px){.mw-parser-output .portalleft{clear:left;float:left;margin:0.5em 1em 0.5em 0}.mw-parser-output .portalright{clear:right;float:right;margin:0.5em 0 0.5em 1em}}html.skin-theme-clientpref-night .mw-parser-output .portalbox{background:transparent}@media(prefers-color-scheme:dark){html.skin-theme-clientpref-os .mw-parser-output .pane{background:transparent}}</style><ul aria-label="Portals" class="noprint portalbox portalborder portalright" role="navigation">
<li class="portalbox-entry"><span class="portalbox-image"><span class="noviewer" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="28" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Industry5.svg/28px-Industry5.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Industry5.svg/42px-Industry5.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Industry5.svg/56px-Industry5.svg.png 2x" width="28"/></span></span></span><span class="portalbox-link"><a href="/wiki/Portal:Companies" title="Portal:Companies">Companies portal</a></span></li></ul>
<ul><li><a href="/wiki/List_of_largest_private_non-governmental_companies_by_revenue" title="List of largest private non-governmental companies by revenue">List of largest private non-governmental companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_companies_in_Africa_by_revenue" title="List of largest companies in Africa by revenue">List of largest companies in Africa by revenue</a></li>
<li><a href="/wiki/List_of_largest_companies_in_Asia" title="List of largest companies in Asia">List of largest companies in Asia</a></li>
<li><a href="/wiki/List_of_largest_companies_in_Europe_by_revenue" title="List of largest companies in Europe by revenue">List of largest companies in Europe by revenue</a></li>
<li><a href="/wiki/Forbes_Global_2000" title="Forbes Global 2000">Forbes Global 2000</a></li>
<li><a href="/wiki/List_of_largest_employers" title="List of largest employers">List of largest employers</a></li>
<li><a href="/wiki/List_of_public_corporations_by_market_capitalization" title="List of public corporations by market capitalization">List of public corporations by market capitalization</a></li>
<li><a href="/wiki/List_of_most_valuable_brands" title="List of most valuable brands">List of most valuable brands</a></li>
<li><a href="/wiki/List_of_companies_by_research_and_development_spending" title="List of companies by research and development spending">List of companies by research and development spending</a></li>
<li><a href="/wiki/List_of_wealthiest_religious_organizations" title="List of wealthiest religious organizations">List of wealthiest religious organizations</a></li>
<li><a href="/wiki/List_of_the_largest_software_companies" title="List of the largest software companies">List of the largest software companies</a></li>
<li><a href="/wiki/List_of_largest_Internet_companies" title="List of largest Internet companies">List of largest Internet companies</a></li>
<li><a href="/wiki/List_of_largest_technology_companies_by_revenue" title="List of largest technology companies by revenue">List of largest technology companies by revenue</a></li>
<li><a href="/wiki/Largest_airlines_in_the_world" title="Largest airlines in the world">Largest airlines in the world</a></li></ul>
<h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit&amp;section=5" title="Edit section: References"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<link href="mw-data:TemplateStyles:r1217336898" rel="mw-deduplicated-inline-style"/><div class="reflist reflist-columns references-column-width" style="column-width: 30em;">
<ol class="references">
<li id="cite_note-W-1"><span class="mw-cite-backlink">^ <a href="#cite_ref-W_1-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-W_1-1"><sup><i><b>b</b></i></sup></a> <a href="#cite_ref-W_1-2"><sup><i><b>c</b></i></sup></a></span> <span class="reference-text"><style data-mw-deduplicate="TemplateStyles:r1215172403">.mw-parser-output cite.citation{font-style:inherit;word-wrap:break-word}.mw-parser-output .citation q{quotes:"\"""\"""'""'"}.mw-parser-output .citation:target{background-color:rgba(0,127,255,0.133)}.mw-parser-output .id-lock-free.id-lock-free a{background:url("//upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg")right 0.1em center/9px no-repeat}body:not(.skin-timeless):not(.skin-minerva) .mw-parser-output .id-lock-free a{background-size:contain}.mw-parser-output .id-lock-limited.id-lock-limited a,.mw-parser-output .id-lock-registration.id-lock-registration a{background:url("//upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg")right 0.1em center/9px no-repeat}body:not(.skin-timeless):not(.skin-minerva) .mw-parser-output .id-lock-limited a,body:not(.skin-timeless):not(.skin-minerva) .mw-parser-output .id-lock-registration a{background-size:contain}.mw-parser-output .id-lock-subscription.id-lock-subscription a{background:url("//upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg")right 0.1em center/9px no-repeat}body:not(.skin-timeless):not(.skin-minerva) .mw-parser-output .id-lock-subscription a{background-size:contain}.mw-parser-output .cs1-ws-icon a{background:url("//upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg")right 0.1em center/12px no-repeat}body:not(.skin-timeless):not(.skin-minerva) .mw-parser-output .cs1-ws-icon a{background-size:contain}.mw-parser-output .cs1-code{color:inherit;background:inherit;border:none;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;color:#d33}.mw-parser-output .cs1-visible-error{color:#d33}.mw-parser-output .cs1-maint{display:none;color:#2C882D;margin-left:0.3em}.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right{padding-right:0.2em}.mw-parser-output .citation .mw-selflink{font-weight:inherit}html.skin-theme-clientpref-night .mw-parser-output .cs1-maint{color:#18911F}html.skin-theme-clientpref-night .mw-parser-output .cs1-visible-error,html.skin-theme-clientpref-night .mw-parser-output .cs1-hidden-error{color:#f8a397}@media(prefers-color-scheme:dark){html.skin-theme-clientpref-os .mw-parser-output .cs1-visible-error,html.skin-theme-clientpref-os .mw-parser-output .cs1-hidden-error{color:#f8a397}html.skin-theme-clientpref-os .mw-parser-output .cs1-maint{color:#18911F}}</style><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/walmart/global500/" rel="nofollow">"Walmart"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Walmart&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fwalmart%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-Fortune_500-2"><span class="mw-cite-backlink">^ <a href="#cite_ref-Fortune_500_2-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-Fortune_500_2-1"><sup><i><b>b</b></i></sup></a></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/global500/2022/" rel="nofollow">"Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-25</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fglobal500%2F2022%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b><a href="#cite_ref-3">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation news cs1"><a class="external text" href="https://fortune.com/franchise-list-page/global-500-methodology-2021" rel="nofollow">"Methodology for Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Fortune&amp;rft.atitle=Methodology+for+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Ffranchise-list-page%2Fglobal-500-methodology-2021&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-5"><span class="mw-cite-backlink"><b><a href="#cite_ref-5">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/saudi-aramco/global500/" rel="nofollow">"Saudi Aramco"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Saudi+Aramco&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fsaudi-aramco%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-6"><span class="mw-cite-backlink"><b><a href="#cite_ref-6">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://s2.q4cdn.com/299287126/files/doc_financials/2023/q4/c7c14359-36fa-40c3-b3ca-5bf7f3fa0b96.pdf" rel="nofollow">"Amazon 2023 10-K"</a> <span class="cs1-format">(PDF)</span>. <i>amazon.com</i>. Amazon. 2024-02-01<span class="reference-accessdate">. Retrieved <span class="nowrap">2024-02-12</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=amazon.com&amp;rft.atitle=Amazon+2023+10-K&amp;rft.date=2024-02-01&amp;rft_id=https%3A%2F%2Fs2.q4cdn.com%2F299287126%2Ffiles%2Fdoc_financials%2F2023%2Fq4%2Fc7c14359-36fa-40c3-b3ca-5bf7f3fa0b96.pdf&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-7"><span class="mw-cite-backlink"><b><a href="#cite_ref-7">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/state-grid/global500/" rel="nofollow">"State Grid"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=State+Grid&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fstate-grid%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-8"><span class="mw-cite-backlink"><b><a href="#cite_ref-8">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1" id="CITEREFMcNair2023">McNair, Ros (2023-03-20). <a class="external text" href="https://www.vitol.com/vitol-2022-volumes-and-review/" rel="nofollow">"Vitol 2022 volumes and review"</a>. <i>Vitol.com</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2023-08-04</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Vitol.com&amp;rft.atitle=Vitol+2022+volumes+and+review&amp;rft.date=2023-03-20&amp;rft.aulast=McNair&amp;rft.aufirst=Ros&amp;rft_id=https%3A%2F%2Fwww.vitol.com%2Fvitol-2022-volumes-and-review%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-9"><span class="mw-cite-backlink"><b><a href="#cite_ref-9">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation news cs1" id="CITEREFHookSheppard2023">Hook, Leslie; Sheppard, David (2023-03-30). <a class="external text" href="https://www.ft.com/content/efdabd7f-949e-4016-a099-c13c99960ed0" rel="nofollow">"Vitol profits soar to record $15bn on back of energy crisis"</a>. <i>Financial Times</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2023-08-04</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Financial+Times&amp;rft.atitle=Vitol+profits+soar+to+record+%2415bn+on+back+of+energy+crisis&amp;rft.date=2023-03-30&amp;rft.aulast=Hook&amp;rft.aufirst=Leslie&amp;rft.au=Sheppard%2C+David&amp;rft_id=https%3A%2F%2Fwww.ft.com%2Fcontent%2Fefdabd7f-949e-4016-a099-c13c99960ed0&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-10"><span class="mw-cite-backlink"><b><a href="#cite_ref-10">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-national-petroleum/global500/" rel="nofollow">"China National Petroleum"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+National+Petroleum&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-national-petroleum%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-11"><span class="mw-cite-backlink"><b><a href="#cite_ref-11">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/sinopec-group/global500/" rel="nofollow">"Sinopec Group"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Sinopec+Group&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fsinopec-group%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-:0-12"><span class="mw-cite-backlink"><b><a href="#cite_ref-:0_12-0">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/exxon-mobil/global500/" rel="nofollow">"Exxon Mobil"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Exxon+Mobil&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fexxon-mobil%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-13"><span class="mw-cite-backlink"><b><a href="#cite_ref-13">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/apple/global500/" rel="nofollow">"Apple"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Apple&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fapple%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-14"><span class="mw-cite-backlink"><b><a href="#cite_ref-14">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/royal-dutch-shell/global500/" rel="nofollow">"Shell"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Shell&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Froyal-dutch-shell%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-15"><span class="mw-cite-backlink"><b><a href="#cite_ref-15">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/unitedhealth-group/global500/" rel="nofollow">"UnitedHealth Group"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=UnitedHealth+Group&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Funitedhealth-group%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-16"><span class="mw-cite-backlink"><b><a href="#cite_ref-16">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/cvs-health/global500/" rel="nofollow">"CVS Health"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=CVS+Health&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fcvs-health%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-17"><span class="mw-cite-backlink"><b><a href="#cite_ref-17">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/trafigura-group/global500/" rel="nofollow">"Trafigura Group"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Trafigura+Group&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Ftrafigura-group%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-18"><span class="mw-cite-backlink"><b><a href="#cite_ref-18">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-state-construction-engineering/global500/" rel="nofollow">"China State Construction Engineering"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+State+Construction+Engineering&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-state-construction-engineering%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-19"><span class="mw-cite-backlink"><b><a href="#cite_ref-19">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/berkshire-hathaway/global500/" rel="nofollow">"Berkshire Hathaway"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Berkshire+Hathaway&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fberkshire-hathaway%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-20"><span class="mw-cite-backlink"><b><a href="#cite_ref-20">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/volkswagen/global500/" rel="nofollow">"Volkswagen"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Volkswagen&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fvolkswagen%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-21"><span class="mw-cite-backlink"><b><a href="#cite_ref-21">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/uniper/global500/" rel="nofollow">"Uniper"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Uniper&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Funiper%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-22"><span class="mw-cite-backlink"><b><a href="#cite_ref-22">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/alphabet/global500/" rel="nofollow">"Alphabet"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Alphabet&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Falphabet%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-23"><span class="mw-cite-backlink"><b><a href="#cite_ref-23">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/mckesson/global500/" rel="nofollow">"McKesson"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=McKesson&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fmckesson%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-24"><span class="mw-cite-backlink"><b><a href="#cite_ref-24">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/toyota-motor/global500/" rel="nofollow">"Toyota Motor"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Toyota+Motor&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Ftoyota-motor%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-25"><span class="mw-cite-backlink"><b><a href="#cite_ref-25">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/total/global500/" rel="nofollow">"Total Company Profile, News, Rankings"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">25 August</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Total+Company+Profile%2C+News%2C+Rankings&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Ftotal%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-26"><span class="mw-cite-backlink"><b><a href="#cite_ref-26">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/glencore/global500/" rel="nofollow">"Glencore"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Glencore&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fglencore%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-27"><span class="mw-cite-backlink"><b><a href="#cite_ref-27">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/bp/global500/" rel="nofollow">"BP"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=BP&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fbp%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-28"><span class="mw-cite-backlink"><b><a href="#cite_ref-28">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/chevron/global500/" rel="nofollow">"Chevron | 2022 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Chevron+%7C+2022+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchevron%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-29"><span class="mw-cite-backlink"><b><a href="#cite_ref-29">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/amerisourcebergen/global500/" rel="nofollow">"AmerisourceBergen"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=AmerisourceBergen&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Famerisourcebergen%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-30"><span class="mw-cite-backlink"><b><a href="#cite_ref-30">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/samsung-electronics/global500/" rel="nofollow">"Samsung Electronics"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Samsung+Electronics&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fsamsung-electronics%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-31"><span class="mw-cite-backlink"><b><a href="#cite_ref-31">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/costco/global500/" rel="nofollow">"Costco Wholesale"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Costco+Wholesale&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fcostco%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-32"><span class="mw-cite-backlink"><b><a href="#cite_ref-32">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/hon-hai-precision-industry/global500/" rel="nofollow">"Hon Hai Precision Industry"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Hon+Hai+Precision+Industry&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fhon-hai-precision-industry%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-33"><span class="mw-cite-backlink"><b><a href="#cite_ref-33">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/industrial-commercial-bank-of-china/global500/" rel="nofollow">"Industrial &amp; Commercial Bank of China"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Industrial+%26+Commercial+Bank+of+China&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Findustrial-commercial-bank-of-china%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-34"><span class="mw-cite-backlink"><b><a href="#cite_ref-34">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://www.microsoft.com/en-us/Investor/earnings/FY-2023-Q4/" rel="nofollow">"FY23 Q4 - Press Releases - Investor Relations - Microsoft"</a>. <i>www.microsoft.com</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2023-12-25</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=www.microsoft.com&amp;rft.atitle=FY23+Q4+-+Press+Releases+-+Investor+Relations+-+Microsoft&amp;rft_id=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2FInvestor%2Fearnings%2FFY-2023-Q4%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-35"><span class="mw-cite-backlink"><b><a href="#cite_ref-35">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-construction-bank/global500/" rel="nofollow">"China Construction Bank"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+Construction+Bank&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-construction-bank%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-36"><span class="mw-cite-backlink"><b><a href="#cite_ref-36">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/stellantis/global500/" rel="nofollow">"Stellantis | 2022 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Stellantis+%7C+2022+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fstellantis%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-37"><span class="mw-cite-backlink"><b><a href="#cite_ref-37">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/agricultural-bank-of-china/global500/" rel="nofollow">"Agricultural Bank of China"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Agricultural+Bank+of+China&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fagricultural-bank-of-china%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-38"><span class="mw-cite-backlink"><b><a href="#cite_ref-38">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/ping-an-insurance/global500/" rel="nofollow">"Ping An Insurance"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Ping+An+Insurance&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fping-an-insurance%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-39"><span class="mw-cite-backlink"><b><a href="#cite_ref-39">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/cardinal-health/global500/" rel="nofollow">"Cardinal Health"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Cardinal+Health&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fcardinal-health%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-40"><span class="mw-cite-backlink"><b><a href="#cite_ref-40">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/cigna/global500/" rel="nofollow">"Cigna"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Cigna&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fcigna%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-41"><span class="mw-cite-backlink"><b><a href="#cite_ref-41">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/marathon-petroleum/global500/" rel="nofollow">"Marathon Petroleum | 2022 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Marathon+Petroleum+%7C+2022+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fmarathon-petroleum%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-42"><span class="mw-cite-backlink"><b><a href="#cite_ref-42">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/phillips/fortune500/" rel="nofollow">"Phillips 66"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Phillips+66&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fphillips%2Ffortune500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-43"><span class="mw-cite-backlink"><b><a href="#cite_ref-43">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/sinochem-holdings/global500/" rel="nofollow">"Sinochem Holdings | 2022 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Sinochem+Holdings+%7C+2022+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fsinochem-holdings%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-44"><span class="mw-cite-backlink"><b><a href="#cite_ref-44">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-railway-engineering/global500/" rel="nofollow">"China Railway Engineering Group"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+Railway+Engineering+Group&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-railway-engineering%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-:2-45"><span class="mw-cite-backlink"><b><a href="#cite_ref-:2_45-0">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/valero-energy/fortune500/" rel="nofollow">"Valero Energy"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Valero+Energy&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fvalero-energy%2Ffortune500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-46"><span class="mw-cite-backlink"><b><a href="#cite_ref-46">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/gazprom/global500/" rel="nofollow">"Gazprom | 2023 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Gazprom+%7C+2023+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fgazprom%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-47"><span class="mw-cite-backlink"><b><a href="#cite_ref-47">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1" id="CITEREFMurphy">Murphy, Andrea. <a class="external text" href="https://www.forbes.com/lists/largest-private-companies/" rel="nofollow">"America's Largest Private Companies 2022"</a>. <i>Forbes</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2023-08-04</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Forbes&amp;rft.atitle=America%27s+Largest+Private+Companies+2022&amp;rft.aulast=Murphy&amp;rft.aufirst=Andrea&amp;rft_id=https%3A%2F%2Fwww.forbes.com%2Flists%2Flargest-private-companies%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-48"><span class="mw-cite-backlink"><b><a href="#cite_ref-48">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-national-offshore-oil/global500/" rel="nofollow">"China National Offshore Oil"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+National+Offshore+Oil&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-national-offshore-oil%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-49"><span class="mw-cite-backlink"><b><a href="#cite_ref-49">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-railway-construction/global500/" rel="nofollow">"China Railway Construction"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+Railway+Construction&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-railway-construction%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-50"><span class="mw-cite-backlink"><b><a href="#cite_ref-50">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/china-baowu-steel-group/global500/" rel="nofollow">"China Baowu Steel Group | 2022 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=China+Baowu+Steel+Group+%7C+2022+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fchina-baowu-steel-group%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-51"><span class="mw-cite-backlink"><b><a href="#cite_ref-51">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://nrf.com/blog/look-2023-top-50-global-retailers" rel="nofollow">"A look at the 2023 Top 50 Global Retailers"</a>. <i>NRF</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2023-08-04</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=NRF&amp;rft.atitle=A+look+at+the+2023+Top+50+Global+Retailers&amp;rft_id=https%3A%2F%2Fnrf.com%2Fblog%2Flook-2023-top-50-global-retailers&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-52"><span class="mw-cite-backlink"><b><a href="#cite_ref-52">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/mitsubishi/global500/" rel="nofollow">"Mitsubishi | 2022 Global 500"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2022-08-26</span></span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Mitsubishi+%7C+2022+Global+500&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fmitsubishi%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-53"><span class="mw-cite-backlink"><b><a href="#cite_ref-53">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/ford-motor/fortune500/" rel="nofollow">"Ford Motor"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Ford+Motor&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fford-motor%2Ffortune500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
<li id="cite_note-54"><span class="mw-cite-backlink"><b><a href="#cite_ref-54">^</a></b></span> <span class="reference-text"><link href="mw-data:TemplateStyles:r1215172403" rel="mw-deduplicated-inline-style"/><cite class="citation web cs1"><a class="external text" href="https://fortune.com/company/daimler/global500/" rel="nofollow">"Mercedes-Benz Group"</a>. <i>Fortune</i><span class="reference-accessdate">. Retrieved <span class="nowrap">20 June</span> 2022</span>.</cite><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Fortune&amp;rft.atitle=Mercedes-Benz+Group&amp;rft_id=https%3A%2F%2Ffortune.com%2Fcompany%2Fdaimler%2Fglobal500%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AList+of+largest+companies+by+revenue"></span></span>
</li>
</ol></div>
<h2><span class="mw-headline" id="External_links">External links</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_largest_companies_by_revenue&amp;action=edit&amp;section=6" title="Edit section: External links"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a class="external text" href="http://fortune.com/global500/list/" rel="nofollow">Fortune Global 500 List</a></li></ul>
<div class="navbox-styles"><style data-mw-deduplicate="TemplateStyles:r1129693374">.mw-parser-output .hlist dl,.mw-parser-output .hlist ol,.mw-parser-output .hlist ul{margin:0;padding:0}.mw-parser-output .hlist dd,.mw-parser-output .hlist dt,.mw-parser-output .hlist li{margin:0;display:inline}.mw-parser-output .hlist.inline,.mw-parser-output .hlist.inline dl,.mw-parser-output .hlist.inline ol,.mw-parser-output .hlist.inline ul,.mw-parser-output .hlist dl dl,.mw-parser-output .hlist dl ol,.mw-parser-output .hlist dl ul,.mw-parser-output .hlist ol dl,.mw-parser-output .hlist ol ol,.mw-parser-output .hlist ol ul,.mw-parser-output .hlist ul dl,.mw-parser-output .hlist ul ol,.mw-parser-output .hlist ul ul{display:inline}.mw-parser-output .hlist .mw-empty-li{display:none}.mw-parser-output .hlist dt::after{content:": "}.mw-parser-output .hlist dd::after,.mw-parser-output .hlist li::after{content:" · ";font-weight:bold}.mw-parser-output .hlist dd:last-child::after,.mw-parser-output .hlist dt:last-child::after,.mw-parser-output .hlist li:last-child::after{content:none}.mw-parser-output .hlist dd dd:first-child::before,.mw-parser-output .hlist dd dt:first-child::before,.mw-parser-output .hlist dd li:first-child::before,.mw-parser-output .hlist dt dd:first-child::before,.mw-parser-output .hlist dt dt:first-child::before,.mw-parser-output .hlist dt li:first-child::before,.mw-parser-output .hlist li dd:first-child::before,.mw-parser-output .hlist li dt:first-child::before,.mw-parser-output .hlist li li:first-child::before{content:" (";font-weight:normal}.mw-parser-output .hlist dd dd:last-child::after,.mw-parser-output .hlist dd dt:last-child::after,.mw-parser-output .hlist dd li:last-child::after,.mw-parser-output .hlist dt dd:last-child::after,.mw-parser-output .hlist dt dt:last-child::after,.mw-parser-output .hlist dt li:last-child::after,.mw-parser-output .hlist li dd:last-child::after,.mw-parser-output .hlist li dt:last-child::after,.mw-parser-output .hlist li li:last-child::after{content:")";font-weight:normal}.mw-parser-output .hlist ol{counter-reset:listitem}.mw-parser-output .hlist ol>li{counter-increment:listitem}.mw-parser-output .hlist ol>li::before{content:" "counter(listitem)"\a0 "}.mw-parser-output .hlist dd ol>li:first-child::before,.mw-parser-output .hlist dt ol>li:first-child::before,.mw-parser-output .hlist li ol>li:first-child::before{content:" ("counter(listitem)"\a0 "}</style><style data-mw-deduplicate="TemplateStyles:r1228936124">.mw-parser-output .navbox{box-sizing:border-box;border:1px solid #a2a9b1;width:100%;clear:both;font-size:88%;text-align:center;padding:1px;margin:1em auto 0}.mw-parser-output .navbox .navbox{margin-top:0}.mw-parser-output .navbox+.navbox,.mw-parser-output .navbox+.navbox-styles+.navbox{margin-top:-1px}.mw-parser-output .navbox-inner,.mw-parser-output .navbox-subgroup{width:100%}.mw-parser-output .navbox-group,.mw-parser-output .navbox-title,.mw-parser-output .navbox-abovebelow{padding:0.25em 1em;line-height:1.5em;text-align:center}.mw-parser-output .navbox-group{white-space:nowrap;text-align:right}.mw-parser-output .navbox,.mw-parser-output .navbox-subgroup{background-color:#fdfdfd}.mw-parser-output .navbox-list{line-height:1.5em;border-color:#fdfdfd}.mw-parser-output .navbox-list-with-group{text-align:left;border-left-width:2px;border-left-style:solid}.mw-parser-output tr+tr>.navbox-abovebelow,.mw-parser-output tr+tr>.navbox-group,.mw-parser-output tr+tr>.navbox-image,.mw-parser-output tr+tr>.navbox-list{border-top:2px solid #fdfdfd}.mw-parser-output .navbox-title{background-color:#ccf}.mw-parser-output .navbox-abovebelow,.mw-parser-output .navbox-group,.mw-parser-output .navbox-subgroup .navbox-title{background-color:#ddf}.mw-parser-output .navbox-subgroup .navbox-group,.mw-parser-output .navbox-subgroup .navbox-abovebelow{background-color:#e6e6ff}.mw-parser-output .navbox-even{background-color:#f7f7f7}.mw-parser-output .navbox-odd{background-color:transparent}.mw-parser-output .navbox .hlist td dl,.mw-parser-output .navbox .hlist td ol,.mw-parser-output .navbox .hlist td ul,.mw-parser-output .navbox td.hlist dl,.mw-parser-output .navbox td.hlist ol,.mw-parser-output .navbox td.hlist ul{padding:0.125em 0}.mw-parser-output .navbox .navbar{display:block;font-size:100%}.mw-parser-output .navbox-title .navbar{float:left;text-align:left;margin-right:0.5em}body.skin--responsive .mw-parser-output .navbox-image img{max-width:none!important}</style></div><div aria-labelledby="Extreme_wealth" class="navbox" role="navigation" style="padding:3px"><table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th class="navbox-title" colspan="2" scope="col"><link href="mw-data:TemplateStyles:r1129693374" rel="mw-deduplicated-inline-style"/><style data-mw-deduplicate="TemplateStyles:r1063604349">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:Wealth" title="Template:Wealth"><abbr title="View this template">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Wealth" title="Template talk:Wealth"><abbr title="Discuss this template">t</abbr></a></li><li class="nv-edit"><a href="/wiki/Special:EditPage/Template:Wealth" title="Special:EditPage/Template:Wealth"><abbr title="Edit this template">e</abbr></a></li></ul></div><div id="Extreme_wealth" style="font-size:114%;margin:0 4em">Extreme <a href="/wiki/Wealth" title="Wealth">wealth</a></div></th></tr><tr><th class="navbox-group" scope="row" style="width:1%">Concepts</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Capital_accumulation" title="Capital accumulation">Capital accumulation</a>
<ul><li><a href="/wiki/Overaccumulation" title="Overaccumulation">Overaccumulation</a></li></ul></li>
<li><a href="/wiki/Economic_inequality" title="Economic inequality">Economic inequality</a>
<ul><li><a class="mw-redirect" href="/wiki/Wealth_distribution" title="Wealth distribution">Wealth distribution</a></li>
<li><a href="/wiki/Income_distribution" title="Income distribution">Income distribution</a></li>
<li><a href="/wiki/Consumption_distribution" title="Consumption distribution">Consumption distribution</a></li>
<li><a href="/wiki/History_of_economic_inequality" title="History of economic inequality">History of economic inequality</a></li></ul></li>
<li><a href="/wiki/International_inequality" title="International inequality">International inequality</a></li>
<li><a href="/wiki/Elite" title="Elite">Elite</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarchy</a></li>
<li><a href="/wiki/Overclass" title="Overclass">Overclass</a></li>
<li><a href="/wiki/Plutocracy" title="Plutocracy">Plutocracy</a></li>
<li><a href="/wiki/Plutonomy" title="Plutonomy">Plutonomy</a>
<ul><li><ul><li><a href="/wiki/Primitive_accumulation_of_capital" title="Primitive accumulation of capital">Primitive accumulation of capital</a></li></ul></li></ul></li>
<li><a href="/wiki/Upper_class" title="Upper class">Upper class</a>
<ul><li><a href="/wiki/Nouveau_riche" title="Nouveau riche"><i>Nouveau riche</i> <wbr/>(new money)</a></li>
<li><a href="/wiki/Old_money" title="Old money"><i>Vieux riche</i> <wbr/>(old money)</a></li></ul></li>
<li><a class="mw-redirect" href="/wiki/Luxury_good" title="Luxury good">Luxury goods</a>
<ul><li><a href="/wiki/Veblen_good" title="Veblen good">Veblen goods</a>
<ul><li><a href="/wiki/Conspicuous_consumption" title="Conspicuous consumption">Conspicuous consumption</a></li>
<li><a href="/wiki/Conspicuous_leisure" title="Conspicuous leisure">Conspicuous leisure</a></li></ul></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">People</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Billionaire" title="Billionaire">Billionaire</a></li>
<li><a href="/wiki/Captain_of_industry" title="Captain of industry">Captain of industry</a></li>
<li><a href="/wiki/High-net-worth_individual" title="High-net-worth individual">High-net-worth individual</a>
<ul><li><a class="mw-redirect" href="/wiki/Ultra_high-net-worth_individual" title="Ultra high-net-worth individual">UHNWI</a></li></ul></li>
<li><a href="/wiki/Magnate" title="Magnate">Magnate</a>
<ul><li><a href="/wiki/Business_magnate" title="Business magnate">Business</a></li></ul></li>
<li><a href="/wiki/Millionaire" title="Millionaire">Millionaire</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarch</a>
<ul><li><a href="/wiki/Business_oligarch" title="Business oligarch">Business</a></li>
<li><a href="/wiki/Russian_oligarchs" title="Russian oligarchs">Russian</a></li>
<li><a href="/wiki/Ukrainian_oligarchs" title="Ukrainian oligarchs">Ukrainian</a></li></ul></li>
<li><a href="/wiki/Robber_baron_(industrialist)" title="Robber baron (industrialist)">Robber baron</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-redirect" href="/wiki/Wealth_concentration" title="Wealth concentration">Concentration</a></li>
<li><a href="/wiki/Distribution_of_wealth" title="Distribution of wealth">Distribution</a></li>
<li><a class="mw-redirect" href="/wiki/Dynastic_wealth" title="Dynastic wealth">Dynastic</a></li>
<li><a href="/wiki/Wealth_effect" title="Wealth effect">Effect</a></li>
<li><a href="/wiki/Geography_and_wealth" title="Geography and wealth">Geography</a></li>
<li><a href="/wiki/Inheritance" title="Inheritance">Inherited</a></li>
<li><a href="/wiki/Wealth_management" title="Wealth management">Management</a></li>
<li><a class="mw-redirect" href="/wiki/National_wealth" title="National wealth">National</a></li>
<li><a href="/wiki/Paper_wealth" title="Paper wealth">Paper</a></li>
<li><a href="/wiki/Wealth_and_religion" title="Wealth and religion">Religion</a></li>
<li><a href="/wiki/Wealth_tax" title="Wealth tax">Tax</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Lists</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_World%27s_Billionaires" title="The World's Billionaires"><i>Forbes</i> list of billionaires</a></li>
<li><a href="/wiki/List_of_centibillionaires" title="List of centibillionaires">List of centibillionaires</a></li>
<li><a href="/wiki/List_of_female_billionaires" title="List of female billionaires">Female billionaires</a></li>
<li><a href="/wiki/List_of_royalty_by_net_worth" title="List of royalty by net worth">Richest royals</a></li>
<li><a href="/wiki/List_of_richest_Americans_in_history" title="List of richest Americans in history">Wealthiest Americans</a></li>
<li><a href="/wiki/List_of_wealthiest_families" title="List of wealthiest families">Wealthiest families</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-selflink selflink">Largest companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_corporate_profits_and_losses" title="List of largest corporate profits and losses">Largest corporate profits and losses</a></li>
<li><a href="/wiki/List_of_public_corporations_by_market_capitalization" title="List of public corporations by market capitalization">Largest corporations by market capitalization</a></li>
<li><a href="/wiki/List_of_largest_financial_services_companies_by_revenue" title="List of largest financial services companies by revenue">Largest financial services companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_manufacturing_companies_by_revenue" title="List of largest manufacturing companies by revenue">Largest manufacturing companies by revenue</a></li>
<li><a href="/wiki/List_of_the_largest_software_companies" title="List of the largest software companies">Largest software companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_technology_companies_by_revenue" title="List of largest technology companies by revenue">Largest technology companies by revenue</a></li>
<li><a href="/wiki/List_of_wealthiest_charitable_foundations" title="List of wealthiest charitable foundations">Charities</a>
<ul><li><a href="/wiki/List_of_philanthropists" title="List of philanthropists">Philanthropists</a></li></ul></li>
<li>Universities
<ul><li><a href="/wiki/Lists_of_institutions_of_higher_education_by_endowment_size" title="Lists of institutions of higher education by endowment size">Endowment size</a></li>
<li><a href="/wiki/List_of_universities_by_number_of_billionaire_alumni" title="List of universities by number of billionaire alumni">Number of billionaire alumni</a></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Other</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/List_of_cities_by_number_of_billionaires" title="List of cities by number of billionaires">Cities by number of billionaires</a></li>
<li><a class="mw-redirect" href="/wiki/List_of_countries_by_the_number_of_billionaires" title="List of countries by the number of billionaires">Countries by number of billionaires</a></li>
<li><a href="/wiki/List_of_countries_by_total_wealth" title="List of countries by total wealth">Countries by total wealth</a></li>
<li><a href="/wiki/List_of_sovereign_states_by_wealth_inequality" title="List of sovereign states by wealth inequality">Countries by wealth inequality</a></li>
<li><a href="/wiki/Wealth_inequality_in_the_United_States" title="Wealth inequality in the United States">Wealth inequality in the United States</a></li>
<li><a href="/wiki/Income_inequality_in_the_United_States" title="Income inequality in the United States">Income inequality in the United States</a></li>
<li><a href="/wiki/Lists_of_most_expensive_items_by_category" title="Lists of most expensive items by category">Most expensive items</a>
<ul><li><a href="/wiki/Category:Lists_of_most_expensive_things" title="Category:Lists of most expensive things">by category</a></li></ul></li>
<li><a href="/wiki/List_of_wealthiest_animals" title="List of wealthiest animals">Wealthiest animals</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Related</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Diseases_of_affluence" title="Diseases of affluence">Diseases of affluence</a>
<ul><li><a href="/wiki/Affluenza" title="Affluenza">Affluenza</a></li>
<li><a href="/wiki/Narcissism#Celebrity_narcissism" title="Narcissism">Acquired situational narcissism</a></li></ul></li>
<li><i><a href="/wiki/Argumentum_ad_crumenam" title="Argumentum ad crumenam">Argumentum ad crumenam</a></i></li>
<li><a href="/wiki/Prosperity_theology" title="Prosperity theology">Prosperity theology</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_Gospel_of_Wealth" title="The Gospel of Wealth">Gospel of Wealth</a></li>
<li><a href="/wiki/The_Giving_Pledge" title="The Giving Pledge">The Giving Pledge</a></li>
<li><a href="/wiki/Philanthrocapitalism" title="Philanthrocapitalism">Philanthrocapitalism</a></li>
<li><a href="/wiki/Venture_philanthropy" title="Venture philanthropy">Venture philanthropy</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Sayings</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_rich_get_richer_and_the_poor_get_poorer" title="The rich get richer and the poor get poorer">The rich get richer and the poor get poorer</a></li>
<li><a href="/wiki/Socialism_for_the_rich_and_capitalism_for_the_poor" title="Socialism for the rich and capitalism for the poor">Socialism for the rich and capitalism for the poor</a></li>
<li><a href="/wiki/Too_big_to_fail" title="Too big to fail">Too big to fail</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Media</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><i><a href="/wiki/Das_Kapital" title="Das Kapital">Das Kapital</a></i></li>
<li><a href="/wiki/Plutus_(play)" title="Plutus (play)"><i>Plutus</i></a>
<ul><li><a href="/wiki/Plutus" title="Plutus">Greek god of wealth</a></li></ul></li>
<li><a href="/wiki/Superclass_(book)" title="Superclass (book)"><i>Superclass</i></a>
<ul><li><a href="/wiki/The_Superclass_List" title="The Superclass List">List</a></li></ul></li>
<li><i><a href="/wiki/The_Theory_of_the_Leisure_Class" title="The Theory of the Leisure Class">The Theory of the Leisure Class</a></i></li>
<li><a href="/wiki/Wealth_(film)" title="Wealth (film)"><i>Wealth</i></a></li>
<li><i><a href="/wiki/The_Wealth_of_Nations" title="The Wealth of Nations">The Wealth of Nations</a></i></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><td class="navbox-abovebelow" colspan="2"><div>
<ul><li><a href="/wiki/Category:Wealth" title="Category:Wealth">Category</a>
<ul><li><a href="/wiki/Category:Wealth_by_country" title="Category:Wealth by country">by country</a></li></ul></li></ul>
</div></td></tr></tbody></table></div>
<!-- 
NewPP limit report
Parsed by mw‐web.codfw.main‐84d7b9664b‐vszzw
Cached time: 20240703203223
Cache expiry: 2592000
Reduced expiry: false
Complications: [vary‐revision‐sha1, show‐toc]
CPU time usage: 0.964 seconds
Real time usage: 1.160 seconds
Preprocessor visited node count: 11762/1000000
Post‐expand include size: 156161/2097152 bytes
Template argument size: 12765/2097152 bytes
Highest expansion depth: 14/100
Expensive parser function count: 2/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 202748/5000000 bytes
Lua time usage: 0.396/10.000 seconds
Lua memory usage: 5867640/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  916.250      1 -total
 34.00%  311.534      2 Template:Reflist
 28.64%  262.372     51 Template:Cite_web
 12.28%  112.549     48 Template:Flagicon
 10.42%   95.457      4 Template:Navbox
 10.37%   95.040      1 Template:Extreme_wealth
  9.10%   83.423      1 Template:Sort_under
  8.11%   74.343      1 Template:Short_description
  7.99%   73.176      1 Template:Sticky_header
  5.11%   46.798      2 Template:Pagetype
-->
<!-- Saved in parser cache with key enwiki:pcache:idhash:997455-0!canonical and timestamp 20240703203223 and revision id 1225623550. Rendering was triggered because: page-view
 -->
</meta></div><!--esi <esi:include src="/esitest-fa8a495983347898/content" /> --><noscript><img alt="" height="1" src="https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" style="border: none; position: absolute;" width="1"/></noscript>
<div class="printfooter" data-nosnippet="">Retrieved from "<a dir="ltr" href="https://en.wikipedia.org/w/index.php?title=List_of_largest_companies_by_revenue&amp;oldid=1225623550">https://en.wikipedia.org/w/index.php?title=List_of_largest_companies_by_revenue&amp;oldid=1225623550</a>"</div></div>
<div class="catlinks" data-mw="interface" id="catlinks"><div class="mw-normal-catlinks" id="mw-normal-catlinks"><a href="/wiki/Help:Category" title="Help:Category">Categories</a>: <ul><li><a href="/wiki/Category:Lists_of_companies_by_revenue" title="Category:Lists of companies by revenue">Lists of companies by revenue</a></li><li><a href="/wiki/Category:Economy-related_lists_of_superlatives" title="Category:Economy-related lists of superlatives">Economy-related lists of superlatives</a></li></ul></div><div class="mw-hidden-catlinks mw-hidden-cats-hidden" id="mw-hidden-catlinks">Hidden categories: <ul><li><a href="/wiki/Category:Articles_with_short_description" title="Category:Articles with short description">Articles with short description</a></li><li><a href="/wiki/Category:Short_description_is_different_from_Wikidata" title="Category:Short description is different from Wikidata">Short description is different from Wikidata</a></li></ul></div></div>
</div>
</main>
</div>
<div class="mw-footer-container">
<footer class="mw-footer" id="footer">
<ul id="footer-info">
<li id="footer-info-lastmod"> This page was last edited on 25 May 2024, at 17:32<span class="anonymous-show"> (UTC)</span>.</li>
<li id="footer-info-copyright">Text is available under the <a href="//en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License" rel="license">Creative Commons Attribution-ShareAlike License 4.0</a><a href="//en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License" rel="license" style="display:none;"></a>;
additional terms may apply. By using this site, you agree to the <a href="//foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use">Terms of Use</a> and <a href="//foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy">Privacy Policy</a>. Wikipedia® is a registered trademark of the <a href="//www.wikimediafoundation.org/">Wikimedia Foundation, Inc.</a>, a non-profit organization.</li>
</ul>
<ul id="footer-places">
<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy">Privacy policy</a></li>
<li id="footer-places-about"><a href="/wiki/Wikipedia:About">About Wikipedia</a></li>
<li id="footer-places-disclaimers"><a href="/wiki/Wikipedia:General_disclaimer">Disclaimers</a></li>
<li id="footer-places-contact"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us">Contact Wikipedia</a></li>
<li id="footer-places-wm-codeofconduct"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct">Code of Conduct</a></li>
<li id="footer-places-developers"><a href="https://developer.wikimedia.org">Developers</a></li>
<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/en.wikipedia.org">Statistics</a></li>
<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement">Cookie statement</a></li>
<li id="footer-places-mobileview"><a class="noprint stopMobileRedirectToggle" href="//en.m.wikipedia.org/w/index.php?title=List_of_largest_companies_by_revenue&amp;mobileaction=toggle_view_mobile">Mobile view</a></li>
</ul>
<ul class="noprint" id="footer-icons">
<li id="footer-copyrightico"><a class="cdx-button cdx-button--fake-button cdx-button--size-large cdx-button--fake-button--enabled" href="https://wikimediafoundation.org/" style="padding-left: 8px; padding-right: 8px;" target="https://wikimediafoundation.org/"><img alt="Wikimedia Foundation" height="29" src="/static/images/footer/wikimedia-button.svg" width="84"/></a></li>
<li id="footer-poweredbyico"><a class="cdx-button cdx-button--fake-button cdx-button--size-large cdx-button--fake-button--enabled" href="https://www.mediawiki.org" style="padding-left: 8px; padding-right: 8px;" target="https://www.mediawiki.org"><img alt="Powered by MediaWiki" height="29" src="/static/images/footer/poweredby_mediawiki.svg" width="84"/></a></li>
</ul>
</footer>
</div>
</div>
</div>
<div class="vector-settings" id="p-dock-bottom">
<ul>
<li>
</li>
</ul>
</div>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgHostname":"mw-web.codfw.main-84d7b9664b-wl8pl","wgBackendResponseTime":111,"wgPageParseReport":{"limitreport":{"cputime":"0.964","walltime":"1.160","ppvisitednodes":{"value":11762,"limit":1000000},"postexpandincludesize":{"value":156161,"limit":2097152},"templateargumentsize":{"value":12765,"limit":2097152},"expansiondepth":{"value":14,"limit":100},"expensivefunctioncount":{"value":2,"limit":500},"unstrip-depth":{"value":1,"limit":20},"unstrip-size":{"value":202748,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  916.250      1 -total"," 34.00%  311.534      2 Template:Reflist"," 28.64%  262.372     51 Template:Cite_web"," 12.28%  112.549     48 Template:Flagicon"," 10.42%   95.457      4 Template:Navbox"," 10.37%   95.040      1 Template:Extreme_wealth","  9.10%   83.423      1 Template:Sort_under","  8.11%   74.343      1 Template:Short_description","  7.99%   73.176      1 Template:Sticky_header","  5.11%   46.798      2 Template:Pagetype"]},"scribunto":{"limitreport-timeusage":{"value":"0.396","limit":"10.000"},"limitreport-memusage":{"value":5867640,"limit":52428800}},"cachereport":{"origin":"mw-web.codfw.main-84d7b9664b-vszzw","timestamp":"20240703203223","ttl":2592000,"transientcontent":false}}});});</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"List of largest companies by revenue","url":"https:\/\/en.wikipedia.org\/wiki\/List_of_largest_companies_by_revenue","sameAs":"http:\/\/www.wikidata.org\/entity\/Q900297","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q900297","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2004-09-19T01:30:49Z","dateModified":"2024-05-25T17:32:53Z","image":"https:\/\/upload.wikimedia.org\/wikipedia\/commons\/d\/d4\/Walmart_store_exterior_5266815680.jpg","headline":"Wikimedia list article"}</script>
</body>
</html>
soup.find_all('table')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
[<table class="wikitable sortable sticky-header-multi sort-under" style="text-align:left;">
<tbody><tr>
<th rowspan="2" scope="col">Rank
</th>
<th rowspan="2" scope="col">Name
</th>
<th rowspan="2" scope="col">Industry
</th>
<th scope="col">Revenue
</th>
<th scope="col">Profit
</th>
<th rowspan="2" scope="col">Employees
</th>
<th rowspan="2" scope="col">Headquarters<sup class="reference" id="cite_ref-4"><a href="#cite_note-4">[note 1]</a></sup>
</th>
<th rowspan="2" scope="col"><a href="/wiki/State-owned_enterprise" title="State-owned enterprise">State-owned</a>
</th>
<th class="unsortable" rowspan="2" scope="col"><abbr title="Reference(s)">Ref.</abbr>
</th>
<th rowspan="2" scope="col">Revenue per worker
</th></tr>
<tr>
<th colspan="2" scope="col"><small>USD millions</small>
</th></tr>
<tr>
<th scope="col">1
</th>
<td><a href="/wiki/Walmart" title="Walmart">Walmart</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $611,289</td>
<td style="text-align:left;">$11,680</td>
<td style="text-align:right;">2,100,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-W_1-2"><a href="#cite_note-W-1">[1]</a></sup>
</td>
<td>$291,090.00
</td></tr>
<tr>
<th scope="row">2
</th>
<td><a href="/wiki/Saudi_Aramco" title="Saudi Aramco">Saudi Aramco</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $603,651</td>
<td style="text-align:left;">$159,069</td>
<td style="text-align:right;">70,496</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Saudi_Arabia" title="Saudi Arabia"><img alt="Saudi Arabia" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></a></span></span> Saudi Arabia</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-5"><a href="#cite_note-5">[4]</a></sup>
</td>
<td>$8,562,911.37
</td></tr>
<tr>
<th scope="row">3
</th>
<td><a href="/wiki/Amazon_(company)" title="Amazon (company)">Amazon</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $574,785</td>
<td style="text-align:left;">$30,425</td>
<td style="text-align:right;">1,525,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-6"><a href="#cite_note-6">[5]</a></sup>
</td>
<td>$376,908.20
</td></tr>
<tr>
<th scope="row">4
</th>
<td><a href="/wiki/State_Grid_Corporation_of_China" title="State Grid Corporation of China">State Grid Corporation of China</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $530,009</td>
<td style="text-align:left;">$8,192</td>
<td style="text-align:right;">870,287
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-7"><a href="#cite_note-7">[6]</a></sup>
</td>
<td>$609,004.85
</td></tr>
<tr>
<th scope="row">5
</th>
<td><a href="/wiki/Vitol" title="Vitol">Vitol</a>
</td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $505,000
</td>
<td>$15,000
</td>
<td style="text-align:right;">1,560
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/15px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/23px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/30px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="15"/></span></span> </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a>
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-8"><a href="#cite_note-8">[7]</a></sup><sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[8]</a></sup>
</td>
<td>$323,717,948.72
</td></tr>
<tr>
<th scope="row">6
</th>
<td><a href="/wiki/China_National_Petroleum_Corporation" title="China National Petroleum Corporation">China National Petroleum Corporation</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $483,019</td>
<td style="text-align:left;">$21,080</td>
<td style="text-align:right;">1,087,049</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-10"><a href="#cite_note-10">[9]</a></sup>
</td>
<td>$444,339.68
</td></tr>
<tr>
<th scope="row">7
</th>
<td><a href="/wiki/China_Petrochemical_Corporation" title="China Petrochemical Corporation">China Petrochemical Corporation</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $471,154</td>
<td style="text-align:left;">$9,657</td>
<td style="text-align:right;">527,487</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[10]</a></sup>
</td>
<td>$893,204.95
</td></tr>
<tr>
<th scope="row">8
</th>
<td><a href="/wiki/ExxonMobil" title="ExxonMobil">ExxonMobil</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $413,680</td>
<td style="text-align:left;">$55,740</td>
<td style="text-align:right;">63,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:0_12-0"><a href="#cite_note-:0-12">[11]</a></sup>
</td>
<td>$6,566,349.21
</td></tr>
<tr>
<th scope="row">9
</th>
<td><a href="/wiki/Apple_Inc." title="Apple Inc.">Apple</a></td>
<td><a href="/wiki/Electronics_industry" title="Electronics industry">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $394,328</td>
<td style="text-align:left;">$99,803</td>
<td style="text-align:right;">164,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-13"><a href="#cite_note-13">[12]</a></sup>
</td>
<td>$2,404,439.02
</td></tr>
<tr>
<th scope="row">10
</th>
<td><a href="/wiki/Shell_plc" title="Shell plc">Shell</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $386,201</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">93,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-14"><a href="#cite_note-14">[13]</a></sup>
</td>
<td>$4,152,698.92
</td></tr>
<tr>
<th scope="row">11
</th>
<td><a href="/wiki/UnitedHealth_Group" title="UnitedHealth Group">UnitedHealth Group</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $324,162</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">400,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-15"><a href="#cite_note-15">[14]</a></sup>
</td>
<td>$810,405.00
</td></tr>
<tr>
<th scope="row">12
</th>
<td><a href="/wiki/CVS_Health" title="CVS Health">CVS Health</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $322,467</td>
<td style="text-align:left;">$4,149</td>
<td style="text-align:right;">259,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-16"><a href="#cite_note-16">[15]</a></sup>
</td>
<td>$1,242,647.40
</td></tr>
<tr>
<th scope="row">13
</th>
<td><a href="/wiki/Trafigura" title="Trafigura">Trafigura</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $318,476</td>
<td style="text-align:left;">$6,994</td>
<td style="text-align:right;">12,347</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Singapore" title="Singapore"><img alt="Singapore" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></a></span></span> Singapore</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-17"><a href="#cite_note-17">[16]</a></sup>
</td>
<td>$25,793,796.06
</td></tr>
<tr>
<th scope="row">14
</th>
<td><a href="/wiki/China_State_Construction_Engineering" title="China State Construction Engineering">China State Construction Engineering</a></td>
<td><a href="/wiki/Construction" title="Construction">Construction</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $305,885</td>
<td style="text-align:left;">$4,234</td>
<td style="text-align:right;">382,492</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-18"><a href="#cite_note-18">[17]</a></sup>
</td>
<td>$799,716.07
</td></tr>
<tr>
<th scope="row">15
</th>
<td><a href="/wiki/Berkshire_Hathaway" title="Berkshire Hathaway">Berkshire Hathaway</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $302,089</td>
<td style="text-align:left;">−$22,819</td>
<td style="text-align:right;">383,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-19"><a href="#cite_note-19">[18]</a></sup>
</td>
<td>$788,744.13
</td></tr>
<tr>
<th scope="row">16
</th>
<td><a href="/wiki/Volkswagen_Group" title="Volkswagen Group">Volkswagen Group</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $293,685</td>
<td style="text-align:left;">$15,233</td>
<td style="text-align:right;">675,805</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-20"><a href="#cite_note-20">[19]</a></sup>
</td>
<td>$434,570.62
</td></tr>
<tr>
<th scope="row">17
</th>
<td><a href="/wiki/Uniper" title="Uniper">Uniper</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $288,309</td>
<td style="text-align:left;">−$19,961</td>
<td style="text-align:right;">7,008</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-21"><a href="#cite_note-21">[20]</a></sup>
</td>
<td>$41,139,982.88
</td></tr>
<tr>
<th scope="row">18
</th>
<td><a href="/wiki/Alphabet_Inc." title="Alphabet Inc.">Alphabet</a></td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $282,836</td>
<td style="text-align:left;">$59,972</td>
<td style="text-align:right;">190,234</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-22"><a href="#cite_note-22">[21]</a></sup>
</td>
<td>$1,486,779.44
</td></tr>
<tr>
<th scope="row">19
</th>
<td><a href="/wiki/McKesson_Corporation" title="McKesson Corporation">McKesson</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $276,711</td>
<td style="text-align:left;">$3,560</td>
<td style="text-align:right;">48,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-23"><a href="#cite_note-23">[22]</a></sup>
</td>
<td>$5,764,812.50
</td></tr>
<tr>
<th scope="row">20
</th>
<td><a href="/wiki/Toyota" title="Toyota">Toyota</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $274,491</td>
<td style="text-align:left;">$18,110</td>
<td style="text-align:right;">375,235</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-24"><a href="#cite_note-24">[23]</a></sup>
</td>
<td>$731,517.58
</td></tr>
<tr>
<th scope="row">21
</th>
<td><a href="/wiki/TotalEnergies" title="TotalEnergies">TotalEnergies</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $263,310</td>
<td style="text-align:left;">$20,526</td>
<td style="text-align:right;">101,279
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/France" title="France"><img alt="France" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></a></span></span> France
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-25"><a href="#cite_note-25">[24]</a></sup>
</td>
<td>$2,599,847.94
</td></tr>
<tr>
<th scope="row">22
</th>
<td><a href="/wiki/Glencore" title="Glencore">Glencore</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $255,984</td>
<td style="text-align:left;">$17,320</td>
<td style="text-align:right;">81,284</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Switzerland" title="Switzerland"><img alt="Switzerland" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></a></span></span> Switzerland</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-26"><a href="#cite_note-26">[25]</a></sup>
</td>
<td>$3,149,254.47
</td></tr>
<tr>
<th scope="row">23
</th>
<td><a href="/wiki/BP" title="BP">BP</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $248,891</td>
<td style="text-align:left;">−$2,487</td>
<td style="text-align:right;">67,600</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-27"><a href="#cite_note-27">[26]</a></sup>
</td>
<td>$3,681,819.53
</td></tr>
<tr>
<th scope="row">24
</th>
<td><a href="/wiki/Chevron_Corporation" title="Chevron Corporation">Chevron</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $246,252</td>
<td style="text-align:left;">$35,465</td>
<td style="text-align:right;">43,846</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-28"><a href="#cite_note-28">[27]</a></sup>
</td>
<td>$5,616,293.39
</td></tr>
<tr>
<th scope="row">25
</th>
<td><a href="/wiki/Cencora" title="Cencora">Cencora</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $238,587</td>
<td style="text-align:left;">$1,699</td>
<td style="text-align:right;">41,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-29"><a href="#cite_note-29">[28]</a></sup>
</td>
<td>$5,749,084.34
</td></tr>
<tr>
<th scope="row">26
</th>
<td><a href="/wiki/Samsung_Electronics" title="Samsung Electronics">Samsung Electronics</a>
</td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $234,129</td>
<td style="text-align:left;">$42,398</td>
<td style="text-align:right;">270,372</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/South_Korea" title="South Korea"><img alt="South Korea" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></a></span></span> South Korea</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-30"><a href="#cite_note-30">[29]</a></sup>
</td>
<td>$865,951.36
</td></tr>
<tr>
<th scope="row">27
</th>
<td><a href="/wiki/Costco" title="Costco">Costco</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $226,954</td>
<td style="text-align:left;">$5,844</td>
<td style="text-align:right;">304,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-31"><a href="#cite_note-31">[30]</a></sup>
</td>
<td>$746,559.21
</td></tr>
<tr>
<th scope="row">28
</th>
<td><a href="/wiki/Foxconn" title="Foxconn">Foxconn</a></td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $222,535</td>
<td style="text-align:left;">$4,751</td>
<td style="text-align:right;">767,062</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Taiwan" title="Taiwan"><img alt="Taiwan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></a></span></span> Taiwan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-32"><a href="#cite_note-32">[31]</a></sup>
</td>
<td>$290,113.45
</td></tr>
<tr>
<th scope="row">29
</th>
<td><a href="/wiki/Industrial_and_Commercial_Bank_of_China" title="Industrial and Commercial Bank of China">Industrial and Commercial Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $214,766</td>
<td style="text-align:left;">$53,589</td>
<td style="text-align:right;">427,587</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-33"><a href="#cite_note-33">[32]</a></sup>
</td>
<td>$502,274.39
</td></tr>
<tr>
<th scope="row">30
</th>
<td><a href="/wiki/Microsoft" title="Microsoft">Microsoft</a>
</td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $211,915
</td>
<td>$73,307
</td>
<td style="text-align:right;">221,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-34"><a href="#cite_note-34">[33]</a></sup>
</td>
<td>$897,149.32
</td></tr>
<tr>
<th scope="row">31
</th>
<td><a href="/wiki/China_Construction_Bank" title="China Construction Bank">China Construction Bank</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $202,753</td>
<td style="text-align:left;">$48,145</td>
<td style="text-align:right;">376,682</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-35"><a href="#cite_note-35">[34]</a></sup>
</td>
<td>$538,260.39
</td></tr>
<tr>
<th>32
</th>
<td><a href="/wiki/Stellantis" title="Stellantis">Stellantis</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $188,888
</td>
<td>$17,669
</td>
<td style="text-align:right">272,367
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Netherlands" title="Netherlands"><img alt="Netherlands" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></a></span></span> Netherlands
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-36"><a href="#cite_note-36">[35]</a></sup>
</td>
<td>$693,505.45
</td></tr>
<tr>
<th scope="row">33
</th>
<td><a href="/wiki/Agricultural_Bank_of_China" title="Agricultural Bank of China">Agricultural Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $187,061</td>
<td style="text-align:left;">$38,524</td>
<td style="text-align:right;">452,258</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-37"><a href="#cite_note-37">[36]</a></sup>
</td>
<td>$413,615.68
</td></tr>
<tr>
<th scope="row">34
</th>
<td><a href="/wiki/Ping_An_Insurance" title="Ping An Insurance">Ping An Insurance</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $181,566</td>
<td style="text-align:left;">$12,454</td>
<td style="text-align:right;">344,223</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-38"><a href="#cite_note-38">[37]</a></sup>
</td>
<td>$527,466.21
</td></tr>
<tr>
<th scope="row">35
</th>
<td><a href="/wiki/Cardinal_Health" title="Cardinal Health">Cardinal Health</a></td>
<td><a href="/wiki/Health_care" title="Health care">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $181,364</td>
<td style="text-align:left;">−$933</td>
<td style="text-align:right;">46,035
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-39"><a href="#cite_note-39">[38]</a></sup>
</td>
<td>$3,939,698.06
</td></tr>
<tr>
<th>36
</th>
<td><a href="/wiki/Cigna" title="Cigna">Cigna</a>
</td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,516
</td>
<td>$6,668
</td>
<td style="text-align:right;">70,231
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-40"><a href="#cite_note-40">[39]</a></sup>
</td>
<td>$2,570,317.95
</td></tr>
<tr>
<th scope="row">37
</th>
<td><a href="/wiki/Marathon_Petroleum" title="Marathon Petroleum">Marathon Petroleum</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,012</td>
<td style="text-align:left;">$14,516</td>
<td style="text-align:right;">17,800</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-41"><a href="#cite_note-41">[40]</a></sup>
</td>
<td>$10,113,033.71
</td></tr>
<tr>
<th scope="row">38
</th>
<td><a href="/wiki/Phillips_66" title="Phillips 66">Phillips 66</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $175,702</td>
<td style="text-align:left;">$11,024</td>
<td style="text-align:right;">13,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-42"><a href="#cite_note-42">[41]</a></sup>
</td>
<td>$13,515,538.46
</td></tr>
<tr>
<th>39
</th>
<td><a href="/wiki/Sinochem" title="Sinochem">Sinochem</a>
</td>
<td><a href="/wiki/Chemical_industry" title="Chemical industry">Chemicals</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $173,834
</td>
<td>–$1
</td>
<td style="text-align:right">220,760
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-43"><a href="#cite_note-43">[42]</a></sup>
</td>
<td>$787,434.32
</td></tr>
<tr>
<th scope="row">40
</th>
<td><a href="/wiki/China_Railway_Engineering_Corporation" title="China Railway Engineering Corporation">China Railway Engineering Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,669
</td>
<td>$2,035
</td>
<td style="text-align:right;">314,792
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-44"><a href="#cite_note-44">[43]</a></sup>
</td>
<td>$545,341.05
</td></tr>
<tr>
<th scope="row">41
</th>
<td><a href="/wiki/Valero_Energy" title="Valero Energy">Valero Energy</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,189</td>
<td style="text-align:left;">$11,528</td>
<td style="text-align:right;">9,743</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:2_45-0"><a href="#cite_note-:2-45">[44]</a></sup>
</td>
<td>$17,570,460.84
</td></tr>
<tr>
<th scope="row">42
</th>
<td><a href="/wiki/Gazprom" title="Gazprom">Gazprom</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $167,832</td>
<td style="text-align:left;">$17,641</td>
<td style="text-align:right;">468,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a>
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-46"><a href="#cite_note-46">[45]</a></sup>
</td>
<td>$358,615.38
</td></tr>
<tr>
<th scope="row">43
</th>
<td><a href="/wiki/Cargill" title="Cargill">Cargill</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $165,000</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">155,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-47"><a href="#cite_note-47">[46]</a></sup>
</td>
<td>$1,064,516.13
</td></tr>
<tr>
<th scope="row">44
</th>
<td><a href="/wiki/China_National_Offshore_Oil_Corporation" title="China National Offshore Oil Corporation">China National Offshore Oil Corporation</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $164,762</td>
<td style="text-align:left;">$16,988</td>
<td style="text-align:right;">81,775</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-48"><a href="#cite_note-48">[47]</a></sup>
</td>
<td>$2,014,821.16
</td></tr>
<tr>
<th scope="row">45
</th>
<td><a href="/wiki/China_Railway_Construction_Corporation" title="China Railway Construction Corporation">China Railway Construction Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $163,037
</td>
<td>$1,800
</td>
<td style="text-align:right;">342,098
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-49"><a href="#cite_note-49">[48]</a></sup>
</td>
<td>$476,579.81
</td></tr>
<tr>
<th scope="row">46
</th>
<td><a href="/wiki/Baowu" title="Baowu">Baowu</a>
</td>
<td><a href="/wiki/Steel" title="Steel">Steel</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $161,698
</td>
<td>$2,493
</td>
<td style="text-align:right;">245,675
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-50"><a href="#cite_note-50">[49]</a></sup>
</td>
<td>$658,178.49
</td></tr>
<tr>
<th scope="row">47
</th>
<td><a href="/wiki/Schwarz_Gruppe" title="Schwarz Gruppe">Schwarz Gruppe</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,800</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">575,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-51"><a href="#cite_note-51">[50]</a></sup>
</td>
<td>$277,913.04
</td></tr>
<tr>
<th>48
</th>
<td><a class="mw-redirect" href="/wiki/Mitsubishi_Group" title="Mitsubishi Group">Mitsubishi Group</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,371
</td>
<td>$8,723
</td>
<td style="text-align:right">79,706
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-52"><a href="#cite_note-52">[51]</a></sup>
</td>
<td>$1,999,485.61
</td></tr>
<tr>
<th scope="row">49
</th>
<td><a href="/wiki/Ford_Motor_Company" title="Ford Motor Company">Ford Motor Company</a></td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $158,057</td>
<td style="text-align:left;">−$1,981</td>
<td style="text-align:right;">173,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-53"><a href="#cite_note-53">[52]</a></sup>
</td>
<td>$913,624.28
</td></tr>
<tr>
<th scope="row">50
</th>
<td><a href="/wiki/Mercedes-Benz_Group" title="Mercedes-Benz Group">Mercedes-Benz Group</a></td>
<td><a href="/wiki/Automotive_industry" title="Automotive industry">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $157,403</td>
<td style="text-align:left;">$15,252</td>
<td style="text-align:right;">168,797</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-54"><a href="#cite_note-54">[53]</a></sup>
</td>
<td>$932,498.80
</td></tr></tbody></table>, <table class="wikitable sortable plainrowheaders" style="text-align: center">
<caption>Breakdown by country
</caption>
<tbody><tr>
<th scope="col">Rank
</th>
<th scope="col">Country
</th>
<th scope="col">Companies
</th></tr>
<tr>
<th scope="row">1
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/United_States" title="United States">United States of America</a></td>
<td>20
</td></tr>
<tr>
<th scope="row">2
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/China" title="China">China</a></td>
<td>13
</td></tr>
<tr>
<th scope="row">3
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Germany" title="Germany">Germany</a></td>
<td>4
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></span></span>  </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Japan" title="Japan">Japan</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Netherlands" title="Netherlands">Netherlands</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/South_Korea" title="South Korea">South Korea</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/France" title="France">France</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Saudi_Arabia" title="Saudi Arabia">Saudi Arabia</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Singapore" title="Singapore">Singapore</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Taiwan" title="Taiwan">Taiwan</a></td>
<td>1
</td></tr></tbody></table>, <table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th class="navbox-title" colspan="2" scope="col"><link href="mw-data:TemplateStyles:r1129693374" rel="mw-deduplicated-inline-style"/><style data-mw-deduplicate="TemplateStyles:r1063604349">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:Wealth" title="Template:Wealth"><abbr title="View this template">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Wealth" title="Template talk:Wealth"><abbr title="Discuss this template">t</abbr></a></li><li class="nv-edit"><a href="/wiki/Special:EditPage/Template:Wealth" title="Special:EditPage/Template:Wealth"><abbr title="Edit this template">e</abbr></a></li></ul></div><div id="Extreme_wealth" style="font-size:114%;margin:0 4em">Extreme <a href="/wiki/Wealth" title="Wealth">wealth</a></div></th></tr><tr><th class="navbox-group" scope="row" style="width:1%">Concepts</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Capital_accumulation" title="Capital accumulation">Capital accumulation</a>
<ul><li><a href="/wiki/Overaccumulation" title="Overaccumulation">Overaccumulation</a></li></ul></li>
<li><a href="/wiki/Economic_inequality" title="Economic inequality">Economic inequality</a>
<ul><li><a class="mw-redirect" href="/wiki/Wealth_distribution" title="Wealth distribution">Wealth distribution</a></li>
<li><a href="/wiki/Income_distribution" title="Income distribution">Income distribution</a></li>
<li><a href="/wiki/Consumption_distribution" title="Consumption distribution">Consumption distribution</a></li>
<li><a href="/wiki/History_of_economic_inequality" title="History of economic inequality">History of economic inequality</a></li></ul></li>
<li><a href="/wiki/International_inequality" title="International inequality">International inequality</a></li>
<li><a href="/wiki/Elite" title="Elite">Elite</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarchy</a></li>
<li><a href="/wiki/Overclass" title="Overclass">Overclass</a></li>
<li><a href="/wiki/Plutocracy" title="Plutocracy">Plutocracy</a></li>
<li><a href="/wiki/Plutonomy" title="Plutonomy">Plutonomy</a>
<ul><li><ul><li><a href="/wiki/Primitive_accumulation_of_capital" title="Primitive accumulation of capital">Primitive accumulation of capital</a></li></ul></li></ul></li>
<li><a href="/wiki/Upper_class" title="Upper class">Upper class</a>
<ul><li><a href="/wiki/Nouveau_riche" title="Nouveau riche"><i>Nouveau riche</i> <wbr/>(new money)</a></li>
<li><a href="/wiki/Old_money" title="Old money"><i>Vieux riche</i> <wbr/>(old money)</a></li></ul></li>
<li><a class="mw-redirect" href="/wiki/Luxury_good" title="Luxury good">Luxury goods</a>
<ul><li><a href="/wiki/Veblen_good" title="Veblen good">Veblen goods</a>
<ul><li><a href="/wiki/Conspicuous_consumption" title="Conspicuous consumption">Conspicuous consumption</a></li>
<li><a href="/wiki/Conspicuous_leisure" title="Conspicuous leisure">Conspicuous leisure</a></li></ul></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">People</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Billionaire" title="Billionaire">Billionaire</a></li>
<li><a href="/wiki/Captain_of_industry" title="Captain of industry">Captain of industry</a></li>
<li><a href="/wiki/High-net-worth_individual" title="High-net-worth individual">High-net-worth individual</a>
<ul><li><a class="mw-redirect" href="/wiki/Ultra_high-net-worth_individual" title="Ultra high-net-worth individual">UHNWI</a></li></ul></li>
<li><a href="/wiki/Magnate" title="Magnate">Magnate</a>
<ul><li><a href="/wiki/Business_magnate" title="Business magnate">Business</a></li></ul></li>
<li><a href="/wiki/Millionaire" title="Millionaire">Millionaire</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarch</a>
<ul><li><a href="/wiki/Business_oligarch" title="Business oligarch">Business</a></li>
<li><a href="/wiki/Russian_oligarchs" title="Russian oligarchs">Russian</a></li>
<li><a href="/wiki/Ukrainian_oligarchs" title="Ukrainian oligarchs">Ukrainian</a></li></ul></li>
<li><a href="/wiki/Robber_baron_(industrialist)" title="Robber baron (industrialist)">Robber baron</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-redirect" href="/wiki/Wealth_concentration" title="Wealth concentration">Concentration</a></li>
<li><a href="/wiki/Distribution_of_wealth" title="Distribution of wealth">Distribution</a></li>
<li><a class="mw-redirect" href="/wiki/Dynastic_wealth" title="Dynastic wealth">Dynastic</a></li>
<li><a href="/wiki/Wealth_effect" title="Wealth effect">Effect</a></li>
<li><a href="/wiki/Geography_and_wealth" title="Geography and wealth">Geography</a></li>
<li><a href="/wiki/Inheritance" title="Inheritance">Inherited</a></li>
<li><a href="/wiki/Wealth_management" title="Wealth management">Management</a></li>
<li><a class="mw-redirect" href="/wiki/National_wealth" title="National wealth">National</a></li>
<li><a href="/wiki/Paper_wealth" title="Paper wealth">Paper</a></li>
<li><a href="/wiki/Wealth_and_religion" title="Wealth and religion">Religion</a></li>
<li><a href="/wiki/Wealth_tax" title="Wealth tax">Tax</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Lists</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_World%27s_Billionaires" title="The World's Billionaires"><i>Forbes</i> list of billionaires</a></li>
<li><a href="/wiki/List_of_centibillionaires" title="List of centibillionaires">List of centibillionaires</a></li>
<li><a href="/wiki/List_of_female_billionaires" title="List of female billionaires">Female billionaires</a></li>
<li><a href="/wiki/List_of_royalty_by_net_worth" title="List of royalty by net worth">Richest royals</a></li>
<li><a href="/wiki/List_of_richest_Americans_in_history" title="List of richest Americans in history">Wealthiest Americans</a></li>
<li><a href="/wiki/List_of_wealthiest_families" title="List of wealthiest families">Wealthiest families</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-selflink selflink">Largest companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_corporate_profits_and_losses" title="List of largest corporate profits and losses">Largest corporate profits and losses</a></li>
<li><a href="/wiki/List_of_public_corporations_by_market_capitalization" title="List of public corporations by market capitalization">Largest corporations by market capitalization</a></li>
<li><a href="/wiki/List_of_largest_financial_services_companies_by_revenue" title="List of largest financial services companies by revenue">Largest financial services companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_manufacturing_companies_by_revenue" title="List of largest manufacturing companies by revenue">Largest manufacturing companies by revenue</a></li>
<li><a href="/wiki/List_of_the_largest_software_companies" title="List of the largest software companies">Largest software companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_technology_companies_by_revenue" title="List of largest technology companies by revenue">Largest technology companies by revenue</a></li>
<li><a href="/wiki/List_of_wealthiest_charitable_foundations" title="List of wealthiest charitable foundations">Charities</a>
<ul><li><a href="/wiki/List_of_philanthropists" title="List of philanthropists">Philanthropists</a></li></ul></li>
<li>Universities
<ul><li><a href="/wiki/Lists_of_institutions_of_higher_education_by_endowment_size" title="Lists of institutions of higher education by endowment size">Endowment size</a></li>
<li><a href="/wiki/List_of_universities_by_number_of_billionaire_alumni" title="List of universities by number of billionaire alumni">Number of billionaire alumni</a></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Other</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/List_of_cities_by_number_of_billionaires" title="List of cities by number of billionaires">Cities by number of billionaires</a></li>
<li><a class="mw-redirect" href="/wiki/List_of_countries_by_the_number_of_billionaires" title="List of countries by the number of billionaires">Countries by number of billionaires</a></li>
<li><a href="/wiki/List_of_countries_by_total_wealth" title="List of countries by total wealth">Countries by total wealth</a></li>
<li><a href="/wiki/List_of_sovereign_states_by_wealth_inequality" title="List of sovereign states by wealth inequality">Countries by wealth inequality</a></li>
<li><a href="/wiki/Wealth_inequality_in_the_United_States" title="Wealth inequality in the United States">Wealth inequality in the United States</a></li>
<li><a href="/wiki/Income_inequality_in_the_United_States" title="Income inequality in the United States">Income inequality in the United States</a></li>
<li><a href="/wiki/Lists_of_most_expensive_items_by_category" title="Lists of most expensive items by category">Most expensive items</a>
<ul><li><a href="/wiki/Category:Lists_of_most_expensive_things" title="Category:Lists of most expensive things">by category</a></li></ul></li>
<li><a href="/wiki/List_of_wealthiest_animals" title="List of wealthiest animals">Wealthiest animals</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Related</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Diseases_of_affluence" title="Diseases of affluence">Diseases of affluence</a>
<ul><li><a href="/wiki/Affluenza" title="Affluenza">Affluenza</a></li>
<li><a href="/wiki/Narcissism#Celebrity_narcissism" title="Narcissism">Acquired situational narcissism</a></li></ul></li>
<li><i><a href="/wiki/Argumentum_ad_crumenam" title="Argumentum ad crumenam">Argumentum ad crumenam</a></i></li>
<li><a href="/wiki/Prosperity_theology" title="Prosperity theology">Prosperity theology</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_Gospel_of_Wealth" title="The Gospel of Wealth">Gospel of Wealth</a></li>
<li><a href="/wiki/The_Giving_Pledge" title="The Giving Pledge">The Giving Pledge</a></li>
<li><a href="/wiki/Philanthrocapitalism" title="Philanthrocapitalism">Philanthrocapitalism</a></li>
<li><a href="/wiki/Venture_philanthropy" title="Venture philanthropy">Venture philanthropy</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Sayings</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_rich_get_richer_and_the_poor_get_poorer" title="The rich get richer and the poor get poorer">The rich get richer and the poor get poorer</a></li>
<li><a href="/wiki/Socialism_for_the_rich_and_capitalism_for_the_poor" title="Socialism for the rich and capitalism for the poor">Socialism for the rich and capitalism for the poor</a></li>
<li><a href="/wiki/Too_big_to_fail" title="Too big to fail">Too big to fail</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Media</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><i><a href="/wiki/Das_Kapital" title="Das Kapital">Das Kapital</a></i></li>
<li><a href="/wiki/Plutus_(play)" title="Plutus (play)"><i>Plutus</i></a>
<ul><li><a href="/wiki/Plutus" title="Plutus">Greek god of wealth</a></li></ul></li>
<li><a href="/wiki/Superclass_(book)" title="Superclass (book)"><i>Superclass</i></a>
<ul><li><a href="/wiki/The_Superclass_List" title="The Superclass List">List</a></li></ul></li>
<li><i><a href="/wiki/The_Theory_of_the_Leisure_Class" title="The Theory of the Leisure Class">The Theory of the Leisure Class</a></i></li>
<li><a href="/wiki/Wealth_(film)" title="Wealth (film)"><i>Wealth</i></a></li>
<li><i><a href="/wiki/The_Wealth_of_Nations" title="The Wealth of Nations">The Wealth of Nations</a></i></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><td class="navbox-abovebelow" colspan="2"><div>
<ul><li><a href="/wiki/Category:Wealth" title="Category:Wealth">Category</a>
<ul><li><a href="/wiki/Category:Wealth_by_country" title="Category:Wealth by country">by country</a></li></ul></li></ul>
</div></td></tr></tbody></table>, <table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Capital_accumulation" title="Capital accumulation">Capital accumulation</a>
<ul><li><a href="/wiki/Overaccumulation" title="Overaccumulation">Overaccumulation</a></li></ul></li>
<li><a href="/wiki/Economic_inequality" title="Economic inequality">Economic inequality</a>
<ul><li><a class="mw-redirect" href="/wiki/Wealth_distribution" title="Wealth distribution">Wealth distribution</a></li>
<li><a href="/wiki/Income_distribution" title="Income distribution">Income distribution</a></li>
<li><a href="/wiki/Consumption_distribution" title="Consumption distribution">Consumption distribution</a></li>
<li><a href="/wiki/History_of_economic_inequality" title="History of economic inequality">History of economic inequality</a></li></ul></li>
<li><a href="/wiki/International_inequality" title="International inequality">International inequality</a></li>
<li><a href="/wiki/Elite" title="Elite">Elite</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarchy</a></li>
<li><a href="/wiki/Overclass" title="Overclass">Overclass</a></li>
<li><a href="/wiki/Plutocracy" title="Plutocracy">Plutocracy</a></li>
<li><a href="/wiki/Plutonomy" title="Plutonomy">Plutonomy</a>
<ul><li><ul><li><a href="/wiki/Primitive_accumulation_of_capital" title="Primitive accumulation of capital">Primitive accumulation of capital</a></li></ul></li></ul></li>
<li><a href="/wiki/Upper_class" title="Upper class">Upper class</a>
<ul><li><a href="/wiki/Nouveau_riche" title="Nouveau riche"><i>Nouveau riche</i> <wbr/>(new money)</a></li>
<li><a href="/wiki/Old_money" title="Old money"><i>Vieux riche</i> <wbr/>(old money)</a></li></ul></li>
<li><a class="mw-redirect" href="/wiki/Luxury_good" title="Luxury good">Luxury goods</a>
<ul><li><a href="/wiki/Veblen_good" title="Veblen good">Veblen goods</a>
<ul><li><a href="/wiki/Conspicuous_consumption" title="Conspicuous consumption">Conspicuous consumption</a></li>
<li><a href="/wiki/Conspicuous_leisure" title="Conspicuous leisure">Conspicuous leisure</a></li></ul></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">People</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Billionaire" title="Billionaire">Billionaire</a></li>
<li><a href="/wiki/Captain_of_industry" title="Captain of industry">Captain of industry</a></li>
<li><a href="/wiki/High-net-worth_individual" title="High-net-worth individual">High-net-worth individual</a>
<ul><li><a class="mw-redirect" href="/wiki/Ultra_high-net-worth_individual" title="Ultra high-net-worth individual">UHNWI</a></li></ul></li>
<li><a href="/wiki/Magnate" title="Magnate">Magnate</a>
<ul><li><a href="/wiki/Business_magnate" title="Business magnate">Business</a></li></ul></li>
<li><a href="/wiki/Millionaire" title="Millionaire">Millionaire</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarch</a>
<ul><li><a href="/wiki/Business_oligarch" title="Business oligarch">Business</a></li>
<li><a href="/wiki/Russian_oligarchs" title="Russian oligarchs">Russian</a></li>
<li><a href="/wiki/Ukrainian_oligarchs" title="Ukrainian oligarchs">Ukrainian</a></li></ul></li>
<li><a href="/wiki/Robber_baron_(industrialist)" title="Robber baron (industrialist)">Robber baron</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-redirect" href="/wiki/Wealth_concentration" title="Wealth concentration">Concentration</a></li>
<li><a href="/wiki/Distribution_of_wealth" title="Distribution of wealth">Distribution</a></li>
<li><a class="mw-redirect" href="/wiki/Dynastic_wealth" title="Dynastic wealth">Dynastic</a></li>
<li><a href="/wiki/Wealth_effect" title="Wealth effect">Effect</a></li>
<li><a href="/wiki/Geography_and_wealth" title="Geography and wealth">Geography</a></li>
<li><a href="/wiki/Inheritance" title="Inheritance">Inherited</a></li>
<li><a href="/wiki/Wealth_management" title="Wealth management">Management</a></li>
<li><a class="mw-redirect" href="/wiki/National_wealth" title="National wealth">National</a></li>
<li><a href="/wiki/Paper_wealth" title="Paper wealth">Paper</a></li>
<li><a href="/wiki/Wealth_and_religion" title="Wealth and religion">Religion</a></li>
<li><a href="/wiki/Wealth_tax" title="Wealth tax">Tax</a></li></ul>
</div></td></tr></tbody></table>, <table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_World%27s_Billionaires" title="The World's Billionaires"><i>Forbes</i> list of billionaires</a></li>
<li><a href="/wiki/List_of_centibillionaires" title="List of centibillionaires">List of centibillionaires</a></li>
<li><a href="/wiki/List_of_female_billionaires" title="List of female billionaires">Female billionaires</a></li>
<li><a href="/wiki/List_of_royalty_by_net_worth" title="List of royalty by net worth">Richest royals</a></li>
<li><a href="/wiki/List_of_richest_Americans_in_history" title="List of richest Americans in history">Wealthiest Americans</a></li>
<li><a href="/wiki/List_of_wealthiest_families" title="List of wealthiest families">Wealthiest families</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-selflink selflink">Largest companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_corporate_profits_and_losses" title="List of largest corporate profits and losses">Largest corporate profits and losses</a></li>
<li><a href="/wiki/List_of_public_corporations_by_market_capitalization" title="List of public corporations by market capitalization">Largest corporations by market capitalization</a></li>
<li><a href="/wiki/List_of_largest_financial_services_companies_by_revenue" title="List of largest financial services companies by revenue">Largest financial services companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_manufacturing_companies_by_revenue" title="List of largest manufacturing companies by revenue">Largest manufacturing companies by revenue</a></li>
<li><a href="/wiki/List_of_the_largest_software_companies" title="List of the largest software companies">Largest software companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_technology_companies_by_revenue" title="List of largest technology companies by revenue">Largest technology companies by revenue</a></li>
<li><a href="/wiki/List_of_wealthiest_charitable_foundations" title="List of wealthiest charitable foundations">Charities</a>
<ul><li><a href="/wiki/List_of_philanthropists" title="List of philanthropists">Philanthropists</a></li></ul></li>
<li>Universities
<ul><li><a href="/wiki/Lists_of_institutions_of_higher_education_by_endowment_size" title="Lists of institutions of higher education by endowment size">Endowment size</a></li>
<li><a href="/wiki/List_of_universities_by_number_of_billionaire_alumni" title="List of universities by number of billionaire alumni">Number of billionaire alumni</a></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Other</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/List_of_cities_by_number_of_billionaires" title="List of cities by number of billionaires">Cities by number of billionaires</a></li>
<li><a class="mw-redirect" href="/wiki/List_of_countries_by_the_number_of_billionaires" title="List of countries by the number of billionaires">Countries by number of billionaires</a></li>
<li><a href="/wiki/List_of_countries_by_total_wealth" title="List of countries by total wealth">Countries by total wealth</a></li>
<li><a href="/wiki/List_of_sovereign_states_by_wealth_inequality" title="List of sovereign states by wealth inequality">Countries by wealth inequality</a></li>
<li><a href="/wiki/Wealth_inequality_in_the_United_States" title="Wealth inequality in the United States">Wealth inequality in the United States</a></li>
<li><a href="/wiki/Income_inequality_in_the_United_States" title="Income inequality in the United States">Income inequality in the United States</a></li>
<li><a href="/wiki/Lists_of_most_expensive_items_by_category" title="Lists of most expensive items by category">Most expensive items</a>
<ul><li><a href="/wiki/Category:Lists_of_most_expensive_things" title="Category:Lists of most expensive things">by category</a></li></ul></li>
<li><a href="/wiki/List_of_wealthiest_animals" title="List of wealthiest animals">Wealthiest animals</a></li></ul>
</div></td></tr></tbody></table>, <table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Diseases_of_affluence" title="Diseases of affluence">Diseases of affluence</a>
<ul><li><a href="/wiki/Affluenza" title="Affluenza">Affluenza</a></li>
<li><a href="/wiki/Narcissism#Celebrity_narcissism" title="Narcissism">Acquired situational narcissism</a></li></ul></li>
<li><i><a href="/wiki/Argumentum_ad_crumenam" title="Argumentum ad crumenam">Argumentum ad crumenam</a></i></li>
<li><a href="/wiki/Prosperity_theology" title="Prosperity theology">Prosperity theology</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_Gospel_of_Wealth" title="The Gospel of Wealth">Gospel of Wealth</a></li>
<li><a href="/wiki/The_Giving_Pledge" title="The Giving Pledge">The Giving Pledge</a></li>
<li><a href="/wiki/Philanthrocapitalism" title="Philanthrocapitalism">Philanthrocapitalism</a></li>
<li><a href="/wiki/Venture_philanthropy" title="Venture philanthropy">Venture philanthropy</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Sayings</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_rich_get_richer_and_the_poor_get_poorer" title="The rich get richer and the poor get poorer">The rich get richer and the poor get poorer</a></li>
<li><a href="/wiki/Socialism_for_the_rich_and_capitalism_for_the_poor" title="Socialism for the rich and capitalism for the poor">Socialism for the rich and capitalism for the poor</a></li>
<li><a href="/wiki/Too_big_to_fail" title="Too big to fail">Too big to fail</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Media</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><i><a href="/wiki/Das_Kapital" title="Das Kapital">Das Kapital</a></i></li>
<li><a href="/wiki/Plutus_(play)" title="Plutus (play)"><i>Plutus</i></a>
<ul><li><a href="/wiki/Plutus" title="Plutus">Greek god of wealth</a></li></ul></li>
<li><a href="/wiki/Superclass_(book)" title="Superclass (book)"><i>Superclass</i></a>
<ul><li><a href="/wiki/The_Superclass_List" title="The Superclass List">List</a></li></ul></li>
<li><i><a href="/wiki/The_Theory_of_the_Leisure_Class" title="The Theory of the Leisure Class">The Theory of the Leisure Class</a></i></li>
<li><a href="/wiki/Wealth_(film)" title="Wealth (film)"><i>Wealth</i></a></li>
<li><i><a href="/wiki/The_Wealth_of_Nations" title="The Wealth of Nations">The Wealth of Nations</a></i></li></ul>
</div></td></tr></tbody></table>]
soup.find('table',class_='wikitable sortable sticky-header-multi sort-under')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
<table class="wikitable sortable sticky-header-multi sort-under" style="text-align:left;">
<tbody><tr>
<th rowspan="2" scope="col">Rank
</th>
<th rowspan="2" scope="col">Name
</th>
<th rowspan="2" scope="col">Industry
</th>
<th scope="col">Revenue
</th>
<th scope="col">Profit
</th>
<th rowspan="2" scope="col">Employees
</th>
<th rowspan="2" scope="col">Headquarters<sup class="reference" id="cite_ref-4"><a href="#cite_note-4">[note 1]</a></sup>
</th>
<th rowspan="2" scope="col"><a href="/wiki/State-owned_enterprise" title="State-owned enterprise">State-owned</a>
</th>
<th class="unsortable" rowspan="2" scope="col"><abbr title="Reference(s)">Ref.</abbr>
</th>
<th rowspan="2" scope="col">Revenue per worker
</th></tr>
<tr>
<th colspan="2" scope="col"><small>USD millions</small>
</th></tr>
<tr>
<th scope="col">1
</th>
<td><a href="/wiki/Walmart" title="Walmart">Walmart</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $611,289</td>
<td style="text-align:left;">$11,680</td>
<td style="text-align:right;">2,100,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-W_1-2"><a href="#cite_note-W-1">[1]</a></sup>
</td>
<td>$291,090.00
</td></tr>
<tr>
<th scope="row">2
</th>
<td><a href="/wiki/Saudi_Aramco" title="Saudi Aramco">Saudi Aramco</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $603,651</td>
<td style="text-align:left;">$159,069</td>
<td style="text-align:right;">70,496</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Saudi_Arabia" title="Saudi Arabia"><img alt="Saudi Arabia" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></a></span></span> Saudi Arabia</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-5"><a href="#cite_note-5">[4]</a></sup>
</td>
<td>$8,562,911.37
</td></tr>
<tr>
<th scope="row">3
</th>
<td><a href="/wiki/Amazon_(company)" title="Amazon (company)">Amazon</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $574,785</td>
<td style="text-align:left;">$30,425</td>
<td style="text-align:right;">1,525,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-6"><a href="#cite_note-6">[5]</a></sup>
</td>
<td>$376,908.20
</td></tr>
<tr>
<th scope="row">4
</th>
<td><a href="/wiki/State_Grid_Corporation_of_China" title="State Grid Corporation of China">State Grid Corporation of China</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $530,009</td>
<td style="text-align:left;">$8,192</td>
<td style="text-align:right;">870,287
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-7"><a href="#cite_note-7">[6]</a></sup>
</td>
<td>$609,004.85
</td></tr>
<tr>
<th scope="row">5
</th>
<td><a href="/wiki/Vitol" title="Vitol">Vitol</a>
</td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $505,000
</td>
<td>$15,000
</td>
<td style="text-align:right;">1,560
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/15px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/23px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/30px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="15"/></span></span> </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a>
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-8"><a href="#cite_note-8">[7]</a></sup><sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[8]</a></sup>
</td>
<td>$323,717,948.72
</td></tr>
<tr>
<th scope="row">6
</th>
<td><a href="/wiki/China_National_Petroleum_Corporation" title="China National Petroleum Corporation">China National Petroleum Corporation</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $483,019</td>
<td style="text-align:left;">$21,080</td>
<td style="text-align:right;">1,087,049</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-10"><a href="#cite_note-10">[9]</a></sup>
</td>
<td>$444,339.68
</td></tr>
<tr>
<th scope="row">7
</th>
<td><a href="/wiki/China_Petrochemical_Corporation" title="China Petrochemical Corporation">China Petrochemical Corporation</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $471,154</td>
<td style="text-align:left;">$9,657</td>
<td style="text-align:right;">527,487</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[10]</a></sup>
</td>
<td>$893,204.95
</td></tr>
<tr>
<th scope="row">8
</th>
<td><a href="/wiki/ExxonMobil" title="ExxonMobil">ExxonMobil</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $413,680</td>
<td style="text-align:left;">$55,740</td>
<td style="text-align:right;">63,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:0_12-0"><a href="#cite_note-:0-12">[11]</a></sup>
</td>
<td>$6,566,349.21
</td></tr>
<tr>
<th scope="row">9
</th>
<td><a href="/wiki/Apple_Inc." title="Apple Inc.">Apple</a></td>
<td><a href="/wiki/Electronics_industry" title="Electronics industry">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $394,328</td>
<td style="text-align:left;">$99,803</td>
<td style="text-align:right;">164,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-13"><a href="#cite_note-13">[12]</a></sup>
</td>
<td>$2,404,439.02
</td></tr>
<tr>
<th scope="row">10
</th>
<td><a href="/wiki/Shell_plc" title="Shell plc">Shell</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $386,201</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">93,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-14"><a href="#cite_note-14">[13]</a></sup>
</td>
<td>$4,152,698.92
</td></tr>
<tr>
<th scope="row">11
</th>
<td><a href="/wiki/UnitedHealth_Group" title="UnitedHealth Group">UnitedHealth Group</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $324,162</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">400,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-15"><a href="#cite_note-15">[14]</a></sup>
</td>
<td>$810,405.00
</td></tr>
<tr>
<th scope="row">12
</th>
<td><a href="/wiki/CVS_Health" title="CVS Health">CVS Health</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $322,467</td>
<td style="text-align:left;">$4,149</td>
<td style="text-align:right;">259,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-16"><a href="#cite_note-16">[15]</a></sup>
</td>
<td>$1,242,647.40
</td></tr>
<tr>
<th scope="row">13
</th>
<td><a href="/wiki/Trafigura" title="Trafigura">Trafigura</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $318,476</td>
<td style="text-align:left;">$6,994</td>
<td style="text-align:right;">12,347</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Singapore" title="Singapore"><img alt="Singapore" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></a></span></span> Singapore</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-17"><a href="#cite_note-17">[16]</a></sup>
</td>
<td>$25,793,796.06
</td></tr>
<tr>
<th scope="row">14
</th>
<td><a href="/wiki/China_State_Construction_Engineering" title="China State Construction Engineering">China State Construction Engineering</a></td>
<td><a href="/wiki/Construction" title="Construction">Construction</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $305,885</td>
<td style="text-align:left;">$4,234</td>
<td style="text-align:right;">382,492</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-18"><a href="#cite_note-18">[17]</a></sup>
</td>
<td>$799,716.07
</td></tr>
<tr>
<th scope="row">15
</th>
<td><a href="/wiki/Berkshire_Hathaway" title="Berkshire Hathaway">Berkshire Hathaway</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $302,089</td>
<td style="text-align:left;">−$22,819</td>
<td style="text-align:right;">383,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-19"><a href="#cite_note-19">[18]</a></sup>
</td>
<td>$788,744.13
</td></tr>
<tr>
<th scope="row">16
</th>
<td><a href="/wiki/Volkswagen_Group" title="Volkswagen Group">Volkswagen Group</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $293,685</td>
<td style="text-align:left;">$15,233</td>
<td style="text-align:right;">675,805</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-20"><a href="#cite_note-20">[19]</a></sup>
</td>
<td>$434,570.62
</td></tr>
<tr>
<th scope="row">17
</th>
<td><a href="/wiki/Uniper" title="Uniper">Uniper</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $288,309</td>
<td style="text-align:left;">−$19,961</td>
<td style="text-align:right;">7,008</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-21"><a href="#cite_note-21">[20]</a></sup>
</td>
<td>$41,139,982.88
</td></tr>
<tr>
<th scope="row">18
</th>
<td><a href="/wiki/Alphabet_Inc." title="Alphabet Inc.">Alphabet</a></td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $282,836</td>
<td style="text-align:left;">$59,972</td>
<td style="text-align:right;">190,234</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-22"><a href="#cite_note-22">[21]</a></sup>
</td>
<td>$1,486,779.44
</td></tr>
<tr>
<th scope="row">19
</th>
<td><a href="/wiki/McKesson_Corporation" title="McKesson Corporation">McKesson</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $276,711</td>
<td style="text-align:left;">$3,560</td>
<td style="text-align:right;">48,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-23"><a href="#cite_note-23">[22]</a></sup>
</td>
<td>$5,764,812.50
</td></tr>
<tr>
<th scope="row">20
</th>
<td><a href="/wiki/Toyota" title="Toyota">Toyota</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $274,491</td>
<td style="text-align:left;">$18,110</td>
<td style="text-align:right;">375,235</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-24"><a href="#cite_note-24">[23]</a></sup>
</td>
<td>$731,517.58
</td></tr>
<tr>
<th scope="row">21
</th>
<td><a href="/wiki/TotalEnergies" title="TotalEnergies">TotalEnergies</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $263,310</td>
<td style="text-align:left;">$20,526</td>
<td style="text-align:right;">101,279
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/France" title="France"><img alt="France" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></a></span></span> France
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-25"><a href="#cite_note-25">[24]</a></sup>
</td>
<td>$2,599,847.94
</td></tr>
<tr>
<th scope="row">22
</th>
<td><a href="/wiki/Glencore" title="Glencore">Glencore</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $255,984</td>
<td style="text-align:left;">$17,320</td>
<td style="text-align:right;">81,284</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Switzerland" title="Switzerland"><img alt="Switzerland" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></a></span></span> Switzerland</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-26"><a href="#cite_note-26">[25]</a></sup>
</td>
<td>$3,149,254.47
</td></tr>
<tr>
<th scope="row">23
</th>
<td><a href="/wiki/BP" title="BP">BP</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $248,891</td>
<td style="text-align:left;">−$2,487</td>
<td style="text-align:right;">67,600</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-27"><a href="#cite_note-27">[26]</a></sup>
</td>
<td>$3,681,819.53
</td></tr>
<tr>
<th scope="row">24
</th>
<td><a href="/wiki/Chevron_Corporation" title="Chevron Corporation">Chevron</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $246,252</td>
<td style="text-align:left;">$35,465</td>
<td style="text-align:right;">43,846</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-28"><a href="#cite_note-28">[27]</a></sup>
</td>
<td>$5,616,293.39
</td></tr>
<tr>
<th scope="row">25
</th>
<td><a href="/wiki/Cencora" title="Cencora">Cencora</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $238,587</td>
<td style="text-align:left;">$1,699</td>
<td style="text-align:right;">41,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-29"><a href="#cite_note-29">[28]</a></sup>
</td>
<td>$5,749,084.34
</td></tr>
<tr>
<th scope="row">26
</th>
<td><a href="/wiki/Samsung_Electronics" title="Samsung Electronics">Samsung Electronics</a>
</td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $234,129</td>
<td style="text-align:left;">$42,398</td>
<td style="text-align:right;">270,372</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/South_Korea" title="South Korea"><img alt="South Korea" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></a></span></span> South Korea</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-30"><a href="#cite_note-30">[29]</a></sup>
</td>
<td>$865,951.36
</td></tr>
<tr>
<th scope="row">27
</th>
<td><a href="/wiki/Costco" title="Costco">Costco</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $226,954</td>
<td style="text-align:left;">$5,844</td>
<td style="text-align:right;">304,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-31"><a href="#cite_note-31">[30]</a></sup>
</td>
<td>$746,559.21
</td></tr>
<tr>
<th scope="row">28
</th>
<td><a href="/wiki/Foxconn" title="Foxconn">Foxconn</a></td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $222,535</td>
<td style="text-align:left;">$4,751</td>
<td style="text-align:right;">767,062</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Taiwan" title="Taiwan"><img alt="Taiwan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></a></span></span> Taiwan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-32"><a href="#cite_note-32">[31]</a></sup>
</td>
<td>$290,113.45
</td></tr>
<tr>
<th scope="row">29
</th>
<td><a href="/wiki/Industrial_and_Commercial_Bank_of_China" title="Industrial and Commercial Bank of China">Industrial and Commercial Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $214,766</td>
<td style="text-align:left;">$53,589</td>
<td style="text-align:right;">427,587</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-33"><a href="#cite_note-33">[32]</a></sup>
</td>
<td>$502,274.39
</td></tr>
<tr>
<th scope="row">30
</th>
<td><a href="/wiki/Microsoft" title="Microsoft">Microsoft</a>
</td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $211,915
</td>
<td>$73,307
</td>
<td style="text-align:right;">221,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-34"><a href="#cite_note-34">[33]</a></sup>
</td>
<td>$897,149.32
</td></tr>
<tr>
<th scope="row">31
</th>
<td><a href="/wiki/China_Construction_Bank" title="China Construction Bank">China Construction Bank</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $202,753</td>
<td style="text-align:left;">$48,145</td>
<td style="text-align:right;">376,682</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-35"><a href="#cite_note-35">[34]</a></sup>
</td>
<td>$538,260.39
</td></tr>
<tr>
<th>32
</th>
<td><a href="/wiki/Stellantis" title="Stellantis">Stellantis</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $188,888
</td>
<td>$17,669
</td>
<td style="text-align:right">272,367
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Netherlands" title="Netherlands"><img alt="Netherlands" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></a></span></span> Netherlands
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-36"><a href="#cite_note-36">[35]</a></sup>
</td>
<td>$693,505.45
</td></tr>
<tr>
<th scope="row">33
</th>
<td><a href="/wiki/Agricultural_Bank_of_China" title="Agricultural Bank of China">Agricultural Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $187,061</td>
<td style="text-align:left;">$38,524</td>
<td style="text-align:right;">452,258</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-37"><a href="#cite_note-37">[36]</a></sup>
</td>
<td>$413,615.68
</td></tr>
<tr>
<th scope="row">34
</th>
<td><a href="/wiki/Ping_An_Insurance" title="Ping An Insurance">Ping An Insurance</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $181,566</td>
<td style="text-align:left;">$12,454</td>
<td style="text-align:right;">344,223</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-38"><a href="#cite_note-38">[37]</a></sup>
</td>
<td>$527,466.21
</td></tr>
<tr>
<th scope="row">35
</th>
<td><a href="/wiki/Cardinal_Health" title="Cardinal Health">Cardinal Health</a></td>
<td><a href="/wiki/Health_care" title="Health care">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $181,364</td>
<td style="text-align:left;">−$933</td>
<td style="text-align:right;">46,035
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-39"><a href="#cite_note-39">[38]</a></sup>
</td>
<td>$3,939,698.06
</td></tr>
<tr>
<th>36
</th>
<td><a href="/wiki/Cigna" title="Cigna">Cigna</a>
</td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,516
</td>
<td>$6,668
</td>
<td style="text-align:right;">70,231
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-40"><a href="#cite_note-40">[39]</a></sup>
</td>
<td>$2,570,317.95
</td></tr>
<tr>
<th scope="row">37
</th>
<td><a href="/wiki/Marathon_Petroleum" title="Marathon Petroleum">Marathon Petroleum</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,012</td>
<td style="text-align:left;">$14,516</td>
<td style="text-align:right;">17,800</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-41"><a href="#cite_note-41">[40]</a></sup>
</td>
<td>$10,113,033.71
</td></tr>
<tr>
<th scope="row">38
</th>
<td><a href="/wiki/Phillips_66" title="Phillips 66">Phillips 66</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $175,702</td>
<td style="text-align:left;">$11,024</td>
<td style="text-align:right;">13,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-42"><a href="#cite_note-42">[41]</a></sup>
</td>
<td>$13,515,538.46
</td></tr>
<tr>
<th>39
</th>
<td><a href="/wiki/Sinochem" title="Sinochem">Sinochem</a>
</td>
<td><a href="/wiki/Chemical_industry" title="Chemical industry">Chemicals</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $173,834
</td>
<td>–$1
</td>
<td style="text-align:right">220,760
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-43"><a href="#cite_note-43">[42]</a></sup>
</td>
<td>$787,434.32
</td></tr>
<tr>
<th scope="row">40
</th>
<td><a href="/wiki/China_Railway_Engineering_Corporation" title="China Railway Engineering Corporation">China Railway Engineering Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,669
</td>
<td>$2,035
</td>
<td style="text-align:right;">314,792
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-44"><a href="#cite_note-44">[43]</a></sup>
</td>
<td>$545,341.05
</td></tr>
<tr>
<th scope="row">41
</th>
<td><a href="/wiki/Valero_Energy" title="Valero Energy">Valero Energy</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,189</td>
<td style="text-align:left;">$11,528</td>
<td style="text-align:right;">9,743</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:2_45-0"><a href="#cite_note-:2-45">[44]</a></sup>
</td>
<td>$17,570,460.84
</td></tr>
<tr>
<th scope="row">42
</th>
<td><a href="/wiki/Gazprom" title="Gazprom">Gazprom</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $167,832</td>
<td style="text-align:left;">$17,641</td>
<td style="text-align:right;">468,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a>
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-46"><a href="#cite_note-46">[45]</a></sup>
</td>
<td>$358,615.38
</td></tr>
<tr>
<th scope="row">43
</th>
<td><a href="/wiki/Cargill" title="Cargill">Cargill</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $165,000</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">155,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-47"><a href="#cite_note-47">[46]</a></sup>
</td>
<td>$1,064,516.13
</td></tr>
<tr>
<th scope="row">44
</th>
<td><a href="/wiki/China_National_Offshore_Oil_Corporation" title="China National Offshore Oil Corporation">China National Offshore Oil Corporation</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $164,762</td>
<td style="text-align:left;">$16,988</td>
<td style="text-align:right;">81,775</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-48"><a href="#cite_note-48">[47]</a></sup>
</td>
<td>$2,014,821.16
</td></tr>
<tr>
<th scope="row">45
</th>
<td><a href="/wiki/China_Railway_Construction_Corporation" title="China Railway Construction Corporation">China Railway Construction Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $163,037
</td>
<td>$1,800
</td>
<td style="text-align:right;">342,098
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-49"><a href="#cite_note-49">[48]</a></sup>
</td>
<td>$476,579.81
</td></tr>
<tr>
<th scope="row">46
</th>
<td><a href="/wiki/Baowu" title="Baowu">Baowu</a>
</td>
<td><a href="/wiki/Steel" title="Steel">Steel</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $161,698
</td>
<td>$2,493
</td>
<td style="text-align:right;">245,675
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-50"><a href="#cite_note-50">[49]</a></sup>
</td>
<td>$658,178.49
</td></tr>
<tr>
<th scope="row">47
</th>
<td><a href="/wiki/Schwarz_Gruppe" title="Schwarz Gruppe">Schwarz Gruppe</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,800</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">575,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-51"><a href="#cite_note-51">[50]</a></sup>
</td>
<td>$277,913.04
</td></tr>
<tr>
<th>48
</th>
<td><a class="mw-redirect" href="/wiki/Mitsubishi_Group" title="Mitsubishi Group">Mitsubishi Group</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,371
</td>
<td>$8,723
</td>
<td style="text-align:right">79,706
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-52"><a href="#cite_note-52">[51]</a></sup>
</td>
<td>$1,999,485.61
</td></tr>
<tr>
<th scope="row">49
</th>
<td><a href="/wiki/Ford_Motor_Company" title="Ford Motor Company">Ford Motor Company</a></td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $158,057</td>
<td style="text-align:left;">−$1,981</td>
<td style="text-align:right;">173,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-53"><a href="#cite_note-53">[52]</a></sup>
</td>
<td>$913,624.28
</td></tr>
<tr>
<th scope="row">50
</th>
<td><a href="/wiki/Mercedes-Benz_Group" title="Mercedes-Benz Group">Mercedes-Benz Group</a></td>
<td><a href="/wiki/Automotive_industry" title="Automotive industry">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $157,403</td>
<td style="text-align:left;">$15,252</td>
<td style="text-align:right;">168,797</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-54"><a href="#cite_note-54">[53]</a></sup>
</td>
<td>$932,498.80
</td></tr></tbody></table>
table=soup.find_all('table')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
print(table)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
[<table class="wikitable sortable sticky-header-multi sort-under" style="text-align:left;">
<tbody><tr>
<th rowspan="2" scope="col">Rank
</th>
<th rowspan="2" scope="col">Name
</th>
<th rowspan="2" scope="col">Industry
</th>
<th scope="col">Revenue
</th>
<th scope="col">Profit
</th>
<th rowspan="2" scope="col">Employees
</th>
<th rowspan="2" scope="col">Headquarters<sup class="reference" id="cite_ref-4"><a href="#cite_note-4">[note 1]</a></sup>
</th>
<th rowspan="2" scope="col"><a href="/wiki/State-owned_enterprise" title="State-owned enterprise">State-owned</a>
</th>
<th class="unsortable" rowspan="2" scope="col"><abbr title="Reference(s)">Ref.</abbr>
</th>
<th rowspan="2" scope="col">Revenue per worker
</th></tr>
<tr>
<th colspan="2" scope="col"><small>USD millions</small>
</th></tr>
<tr>
<th scope="col">1
</th>
<td><a href="/wiki/Walmart" title="Walmart">Walmart</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $611,289</td>
<td style="text-align:left;">$11,680</td>
<td style="text-align:right;">2,100,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-W_1-2"><a href="#cite_note-W-1">[1]</a></sup>
</td>
<td>$291,090.00
</td></tr>
<tr>
<th scope="row">2
</th>
<td><a href="/wiki/Saudi_Aramco" title="Saudi Aramco">Saudi Aramco</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $603,651</td>
<td style="text-align:left;">$159,069</td>
<td style="text-align:right;">70,496</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Saudi_Arabia" title="Saudi Arabia"><img alt="Saudi Arabia" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></a></span></span> Saudi Arabia</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-5"><a href="#cite_note-5">[4]</a></sup>
</td>
<td>$8,562,911.37
</td></tr>
<tr>
<th scope="row">3
</th>
<td><a href="/wiki/Amazon_(company)" title="Amazon (company)">Amazon</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $574,785</td>
<td style="text-align:left;">$30,425</td>
<td style="text-align:right;">1,525,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-6"><a href="#cite_note-6">[5]</a></sup>
</td>
<td>$376,908.20
</td></tr>
<tr>
<th scope="row">4
</th>
<td><a href="/wiki/State_Grid_Corporation_of_China" title="State Grid Corporation of China">State Grid Corporation of China</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $530,009</td>
<td style="text-align:left;">$8,192</td>
<td style="text-align:right;">870,287
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-7"><a href="#cite_note-7">[6]</a></sup>
</td>
<td>$609,004.85
</td></tr>
<tr>
<th scope="row">5
</th>
<td><a href="/wiki/Vitol" title="Vitol">Vitol</a>
</td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $505,000
</td>
<td>$15,000
</td>
<td style="text-align:right;">1,560
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/15px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/23px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/30px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="15"/></span></span> </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a>
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-8"><a href="#cite_note-8">[7]</a></sup><sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[8]</a></sup>
</td>
<td>$323,717,948.72
</td></tr>
<tr>
<th scope="row">6
</th>
<td><a href="/wiki/China_National_Petroleum_Corporation" title="China National Petroleum Corporation">China National Petroleum Corporation</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $483,019</td>
<td style="text-align:left;">$21,080</td>
<td style="text-align:right;">1,087,049</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-10"><a href="#cite_note-10">[9]</a></sup>
</td>
<td>$444,339.68
</td></tr>
<tr>
<th scope="row">7
</th>
<td><a href="/wiki/China_Petrochemical_Corporation" title="China Petrochemical Corporation">China Petrochemical Corporation</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $471,154</td>
<td style="text-align:left;">$9,657</td>
<td style="text-align:right;">527,487</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[10]</a></sup>
</td>
<td>$893,204.95
</td></tr>
<tr>
<th scope="row">8
</th>
<td><a href="/wiki/ExxonMobil" title="ExxonMobil">ExxonMobil</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $413,680</td>
<td style="text-align:left;">$55,740</td>
<td style="text-align:right;">63,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:0_12-0"><a href="#cite_note-:0-12">[11]</a></sup>
</td>
<td>$6,566,349.21
</td></tr>
<tr>
<th scope="row">9
</th>
<td><a href="/wiki/Apple_Inc." title="Apple Inc.">Apple</a></td>
<td><a href="/wiki/Electronics_industry" title="Electronics industry">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $394,328</td>
<td style="text-align:left;">$99,803</td>
<td style="text-align:right;">164,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-13"><a href="#cite_note-13">[12]</a></sup>
</td>
<td>$2,404,439.02
</td></tr>
<tr>
<th scope="row">10
</th>
<td><a href="/wiki/Shell_plc" title="Shell plc">Shell</a>
</td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $386,201</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">93,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-14"><a href="#cite_note-14">[13]</a></sup>
</td>
<td>$4,152,698.92
</td></tr>
<tr>
<th scope="row">11
</th>
<td><a href="/wiki/UnitedHealth_Group" title="UnitedHealth Group">UnitedHealth Group</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $324,162</td>
<td style="text-align:left;">$20,120</td>
<td style="text-align:right;">400,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-15"><a href="#cite_note-15">[14]</a></sup>
</td>
<td>$810,405.00
</td></tr>
<tr>
<th scope="row">12
</th>
<td><a href="/wiki/CVS_Health" title="CVS Health">CVS Health</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $322,467</td>
<td style="text-align:left;">$4,149</td>
<td style="text-align:right;">259,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-16"><a href="#cite_note-16">[15]</a></sup>
</td>
<td>$1,242,647.40
</td></tr>
<tr>
<th scope="row">13
</th>
<td><a href="/wiki/Trafigura" title="Trafigura">Trafigura</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $318,476</td>
<td style="text-align:left;">$6,994</td>
<td style="text-align:right;">12,347</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Singapore" title="Singapore"><img alt="Singapore" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></a></span></span> Singapore</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-17"><a href="#cite_note-17">[16]</a></sup>
</td>
<td>$25,793,796.06
</td></tr>
<tr>
<th scope="row">14
</th>
<td><a href="/wiki/China_State_Construction_Engineering" title="China State Construction Engineering">China State Construction Engineering</a></td>
<td><a href="/wiki/Construction" title="Construction">Construction</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $305,885</td>
<td style="text-align:left;">$4,234</td>
<td style="text-align:right;">382,492</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-18"><a href="#cite_note-18">[17]</a></sup>
</td>
<td>$799,716.07
</td></tr>
<tr>
<th scope="row">15
</th>
<td><a href="/wiki/Berkshire_Hathaway" title="Berkshire Hathaway">Berkshire Hathaway</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $302,089</td>
<td style="text-align:left;">−$22,819</td>
<td style="text-align:right;">383,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-19"><a href="#cite_note-19">[18]</a></sup>
</td>
<td>$788,744.13
</td></tr>
<tr>
<th scope="row">16
</th>
<td><a href="/wiki/Volkswagen_Group" title="Volkswagen Group">Volkswagen Group</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $293,685</td>
<td style="text-align:left;">$15,233</td>
<td style="text-align:right;">675,805</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-20"><a href="#cite_note-20">[19]</a></sup>
</td>
<td>$434,570.62
</td></tr>
<tr>
<th scope="row">17
</th>
<td><a href="/wiki/Uniper" title="Uniper">Uniper</a></td>
<td><a href="/wiki/Electric_utility" title="Electric utility">Electricity</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $288,309</td>
<td style="text-align:left;">−$19,961</td>
<td style="text-align:right;">7,008</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-21"><a href="#cite_note-21">[20]</a></sup>
</td>
<td>$41,139,982.88
</td></tr>
<tr>
<th scope="row">18
</th>
<td><a href="/wiki/Alphabet_Inc." title="Alphabet Inc.">Alphabet</a></td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $282,836</td>
<td style="text-align:left;">$59,972</td>
<td style="text-align:right;">190,234</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-22"><a href="#cite_note-22">[21]</a></sup>
</td>
<td>$1,486,779.44
</td></tr>
<tr>
<th scope="row">19
</th>
<td><a href="/wiki/McKesson_Corporation" title="McKesson Corporation">McKesson</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $276,711</td>
<td style="text-align:left;">$3,560</td>
<td style="text-align:right;">48,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-23"><a href="#cite_note-23">[22]</a></sup>
</td>
<td>$5,764,812.50
</td></tr>
<tr>
<th scope="row">20
</th>
<td><a href="/wiki/Toyota" title="Toyota">Toyota</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $274,491</td>
<td style="text-align:left;">$18,110</td>
<td style="text-align:right;">375,235</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-24"><a href="#cite_note-24">[23]</a></sup>
</td>
<td>$731,517.58
</td></tr>
<tr>
<th scope="row">21
</th>
<td><a href="/wiki/TotalEnergies" title="TotalEnergies">TotalEnergies</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $263,310</td>
<td style="text-align:left;">$20,526</td>
<td style="text-align:right;">101,279
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/France" title="France"><img alt="France" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></a></span></span> France
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-25"><a href="#cite_note-25">[24]</a></sup>
</td>
<td>$2,599,847.94
</td></tr>
<tr>
<th scope="row">22
</th>
<td><a href="/wiki/Glencore" title="Glencore">Glencore</a></td>
<td><a href="/wiki/Commodity_market" title="Commodity market">Commodities</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $255,984</td>
<td style="text-align:left;">$17,320</td>
<td style="text-align:right;">81,284</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Switzerland" title="Switzerland"><img alt="Switzerland" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></a></span></span> Switzerland</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-26"><a href="#cite_note-26">[25]</a></sup>
</td>
<td>$3,149,254.47
</td></tr>
<tr>
<th scope="row">23
</th>
<td><a href="/wiki/BP" title="BP">BP</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $248,891</td>
<td style="text-align:left;">−$2,487</td>
<td style="text-align:right;">67,600</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_Kingdom" title="United Kingdom"><img alt="United Kingdom" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></a></span></span> United Kingdom</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-27"><a href="#cite_note-27">[26]</a></sup>
</td>
<td>$3,681,819.53
</td></tr>
<tr>
<th scope="row">24
</th>
<td><a href="/wiki/Chevron_Corporation" title="Chevron Corporation">Chevron</a></td>
<td><a class="mw-redirect" href="/wiki/Oil_and_gas" title="Oil and gas">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $246,252</td>
<td style="text-align:left;">$35,465</td>
<td style="text-align:right;">43,846</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-28"><a href="#cite_note-28">[27]</a></sup>
</td>
<td>$5,616,293.39
</td></tr>
<tr>
<th scope="row">25
</th>
<td><a href="/wiki/Cencora" title="Cencora">Cencora</a></td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $238,587</td>
<td style="text-align:left;">$1,699</td>
<td style="text-align:right;">41,500</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-29"><a href="#cite_note-29">[28]</a></sup>
</td>
<td>$5,749,084.34
</td></tr>
<tr>
<th scope="row">26
</th>
<td><a href="/wiki/Samsung_Electronics" title="Samsung Electronics">Samsung Electronics</a>
</td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $234,129</td>
<td style="text-align:left;">$42,398</td>
<td style="text-align:right;">270,372</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/South_Korea" title="South Korea"><img alt="South Korea" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></a></span></span> South Korea</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-30"><a href="#cite_note-30">[29]</a></sup>
</td>
<td>$865,951.36
</td></tr>
<tr>
<th scope="row">27
</th>
<td><a href="/wiki/Costco" title="Costco">Costco</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $226,954</td>
<td style="text-align:left;">$5,844</td>
<td style="text-align:right;">304,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-31"><a href="#cite_note-31">[30]</a></sup>
</td>
<td>$746,559.21
</td></tr>
<tr>
<th scope="row">28
</th>
<td><a href="/wiki/Foxconn" title="Foxconn">Foxconn</a></td>
<td><a href="/wiki/Electronics" title="Electronics">Electronics</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $222,535</td>
<td style="text-align:left;">$4,751</td>
<td style="text-align:right;">767,062</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Taiwan" title="Taiwan"><img alt="Taiwan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></a></span></span> Taiwan</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-32"><a href="#cite_note-32">[31]</a></sup>
</td>
<td>$290,113.45
</td></tr>
<tr>
<th scope="row">29
</th>
<td><a href="/wiki/Industrial_and_Commercial_Bank_of_China" title="Industrial and Commercial Bank of China">Industrial and Commercial Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $214,766</td>
<td style="text-align:left;">$53,589</td>
<td style="text-align:right;">427,587</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-33"><a href="#cite_note-33">[32]</a></sup>
</td>
<td>$502,274.39
</td></tr>
<tr>
<th scope="row">30
</th>
<td><a href="/wiki/Microsoft" title="Microsoft">Microsoft</a>
</td>
<td><a href="/wiki/Information_technology" title="Information technology">Information technology</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $211,915
</td>
<td>$73,307
</td>
<td style="text-align:right;">221,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-34"><a href="#cite_note-34">[33]</a></sup>
</td>
<td>$897,149.32
</td></tr>
<tr>
<th scope="row">31
</th>
<td><a href="/wiki/China_Construction_Bank" title="China Construction Bank">China Construction Bank</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $202,753</td>
<td style="text-align:left;">$48,145</td>
<td style="text-align:right;">376,682</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-35"><a href="#cite_note-35">[34]</a></sup>
</td>
<td>$538,260.39
</td></tr>
<tr>
<th>32
</th>
<td><a href="/wiki/Stellantis" title="Stellantis">Stellantis</a>
</td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $188,888
</td>
<td>$17,669
</td>
<td style="text-align:right">272,367
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Netherlands" title="Netherlands"><img alt="Netherlands" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></a></span></span> Netherlands
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-36"><a href="#cite_note-36">[35]</a></sup>
</td>
<td>$693,505.45
</td></tr>
<tr>
<th scope="row">33
</th>
<td><a href="/wiki/Agricultural_Bank_of_China" title="Agricultural Bank of China">Agricultural Bank of China</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $187,061</td>
<td style="text-align:left;">$38,524</td>
<td style="text-align:right;">452,258</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-37"><a href="#cite_note-37">[36]</a></sup>
</td>
<td>$413,615.68
</td></tr>
<tr>
<th scope="row">34
</th>
<td><a href="/wiki/Ping_An_Insurance" title="Ping An Insurance">Ping An Insurance</a></td>
<td><a href="/wiki/Financial_services" title="Financial services">Financials</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $181,566</td>
<td style="text-align:left;">$12,454</td>
<td style="text-align:right;">344,223</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-38"><a href="#cite_note-38">[37]</a></sup>
</td>
<td>$527,466.21
</td></tr>
<tr>
<th scope="row">35
</th>
<td><a href="/wiki/Cardinal_Health" title="Cardinal Health">Cardinal Health</a></td>
<td><a href="/wiki/Health_care" title="Health care">Healthcare</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $181,364</td>
<td style="text-align:left;">−$933</td>
<td style="text-align:right;">46,035
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-39"><a href="#cite_note-39">[38]</a></sup>
</td>
<td>$3,939,698.06
</td></tr>
<tr>
<th>36
</th>
<td><a href="/wiki/Cigna" title="Cigna">Cigna</a>
</td>
<td><a class="mw-redirect" href="/wiki/Healthcare" title="Healthcare">Healthcare</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,516
</td>
<td>$6,668
</td>
<td style="text-align:right;">70,231
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-40"><a href="#cite_note-40">[39]</a></sup>
</td>
<td>$2,570,317.95
</td></tr>
<tr>
<th scope="row">37
</th>
<td><a href="/wiki/Marathon_Petroleum" title="Marathon Petroleum">Marathon Petroleum</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $180,012</td>
<td style="text-align:left;">$14,516</td>
<td style="text-align:right;">17,800</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-41"><a href="#cite_note-41">[40]</a></sup>
</td>
<td>$10,113,033.71
</td></tr>
<tr>
<th scope="row">38
</th>
<td><a href="/wiki/Phillips_66" title="Phillips 66">Phillips 66</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $175,702</td>
<td style="text-align:left;">$11,024</td>
<td style="text-align:right;">13,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-42"><a href="#cite_note-42">[41]</a></sup>
</td>
<td>$13,515,538.46
</td></tr>
<tr>
<th>39
</th>
<td><a href="/wiki/Sinochem" title="Sinochem">Sinochem</a>
</td>
<td><a href="/wiki/Chemical_industry" title="Chemical industry">Chemicals</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $173,834
</td>
<td>–$1
</td>
<td style="text-align:right">220,760
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-43"><a href="#cite_note-43">[42]</a></sup>
</td>
<td>$787,434.32
</td></tr>
<tr>
<th scope="row">40
</th>
<td><a href="/wiki/China_Railway_Engineering_Corporation" title="China Railway Engineering Corporation">China Railway Engineering Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,669
</td>
<td>$2,035
</td>
<td style="text-align:right;">314,792
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-44"><a href="#cite_note-44">[43]</a></sup>
</td>
<td>$545,341.05
</td></tr>
<tr>
<th scope="row">41
</th>
<td><a href="/wiki/Valero_Energy" title="Valero Energy">Valero Energy</a></td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $171,189</td>
<td style="text-align:left;">$11,528</td>
<td style="text-align:right;">9,743</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-:2_45-0"><a href="#cite_note-:2-45">[44]</a></sup>
</td>
<td>$17,570,460.84
</td></tr>
<tr>
<th scope="row">42
</th>
<td><a href="/wiki/Gazprom" title="Gazprom">Gazprom</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $167,832</td>
<td style="text-align:left;">$17,641</td>
<td style="text-align:right;">468,000
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a>
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-46"><a href="#cite_note-46">[45]</a></sup>
</td>
<td>$358,615.38
</td></tr>
<tr>
<th scope="row">43
</th>
<td><a href="/wiki/Cargill" title="Cargill">Cargill</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $165,000</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">155,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-47"><a href="#cite_note-47">[46]</a></sup>
</td>
<td>$1,064,516.13
</td></tr>
<tr>
<th scope="row">44
</th>
<td><a href="/wiki/China_National_Offshore_Oil_Corporation" title="China National Offshore Oil Corporation">China National Offshore Oil Corporation</a>
</td>
<td><a href="/wiki/Fossil_fuel" title="Fossil fuel">Oil and gas</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $164,762</td>
<td style="text-align:left;">$16,988</td>
<td style="text-align:right;">81,775</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-48"><a href="#cite_note-48">[47]</a></sup>
</td>
<td>$2,014,821.16
</td></tr>
<tr>
<th scope="row">45
</th>
<td><a href="/wiki/China_Railway_Construction_Corporation" title="China Railway Construction Corporation">China Railway Construction Corporation</a>
</td>
<td><a href="/wiki/Construction" title="Construction">Construction</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $163,037
</td>
<td>$1,800
</td>
<td style="text-align:right;">342,098
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-49"><a href="#cite_note-49">[48]</a></sup>
</td>
<td>$476,579.81
</td></tr>
<tr>
<th scope="row">46
</th>
<td><a href="/wiki/Baowu" title="Baowu">Baowu</a>
</td>
<td><a href="/wiki/Steel" title="Steel">Steel</a>
</td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $161,698
</td>
<td>$2,493
</td>
<td style="text-align:right;">245,675
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> China
</td>
<td class="table-yes2" data-sort-value="Yes" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="Yes"><img alt="Yes" class="mw-file-element" data-file-height="600" data-file-width="600" decoding="async" height="13" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/13px-Black_check.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/20px-Black_check.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Black_check.svg/26px-Black_check.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-50"><a href="#cite_note-50">[49]</a></sup>
</td>
<td>$658,178.49
</td></tr>
<tr>
<th scope="row">47
</th>
<td><a href="/wiki/Schwarz_Gruppe" title="Schwarz Gruppe">Schwarz Gruppe</a></td>
<td><a href="/wiki/Retail" title="Retail">Retail</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,800</td>
<td style="text-align:left;">...</td>
<td style="text-align:right;">575,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-51"><a href="#cite_note-51">[50]</a></sup>
</td>
<td>$277,913.04
</td></tr>
<tr>
<th>48
</th>
<td><a class="mw-redirect" href="/wiki/Mitsubishi_Group" title="Mitsubishi Group">Mitsubishi Group</a>
</td>
<td><a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
</td>
<td><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $159,371
</td>
<td>$8,723
</td>
<td style="text-align:right">79,706
</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Japan" title="Japan"><img alt="Japan" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></a></span></span> Japan
</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span>
</td>
<td><sup class="reference" id="cite_ref-52"><a href="#cite_note-52">[51]</a></sup>
</td>
<td>$1,999,485.61
</td></tr>
<tr>
<th scope="row">49
</th>
<td><a href="/wiki/Ford_Motor_Company" title="Ford Motor Company">Ford Motor Company</a></td>
<td><a class="mw-redirect" href="/wiki/Automotive" title="Automotive">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Increase"><img alt="Increase" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" width="11"/></span></span> $158,057</td>
<td style="text-align:left;">−$1,981</td>
<td style="text-align:right;">173,000</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> United States</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-53"><a href="#cite_note-53">[52]</a></sup>
</td>
<td>$913,624.28
</td></tr>
<tr>
<th scope="row">50
</th>
<td><a href="/wiki/Mercedes-Benz_Group" title="Mercedes-Benz Group">Mercedes-Benz Group</a></td>
<td><a href="/wiki/Automotive_industry" title="Automotive industry">Automotive</a></td>
<td style="text-align:center;"><span typeof="mw:File"><span title="Decrease"><img alt="Decrease" class="mw-file-element" data-file-height="300" data-file-width="300" decoding="async" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/11px-Decrease2.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/17px-Decrease2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Decrease2.svg/22px-Decrease2.svg.png 2x" width="11"/></span></span> $157,403</td>
<td style="text-align:left;">$15,252</td>
<td style="text-align:right;">168,797</td>
<td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Germany" title="Germany"><img alt="Germany" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></a></span></span> Germany</td>
<td class="table-no2" data-sort-value="No" style="vertical-align: middle; text-align: center;"><span class="skin-invert" typeof="mw:File"><span title="No"><img alt="No" class="mw-file-element" data-file-height="600" data-file-width="525" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/13px-Black_x.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/20px-Black_x.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Black_x.svg/26px-Black_x.svg.png 2x" width="13"/></span></span></td>
<td><sup class="reference" id="cite_ref-54"><a href="#cite_note-54">[53]</a></sup>
</td>
<td>$932,498.80
</td></tr></tbody></table>, <table class="wikitable sortable plainrowheaders" style="text-align: center">
<caption>Breakdown by country
</caption>
<tbody><tr>
<th scope="col">Rank
</th>
<th scope="col">Country
</th>
<th scope="col">Companies
</th></tr>
<tr>
<th scope="row">1
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/United_States" title="United States">United States of America</a></td>
<td>20
</td></tr>
<tr>
<th scope="row">2
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/35px-Flag_of_the_People%27s_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/45px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/China" title="China">China</a></td>
<td>13
</td></tr>
<tr>
<th scope="row">3
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/35px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/46px-Flag_of_Germany.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Germany" title="Germany">Germany</a></td>
<td>4
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/35px-Flag_of_the_United_Kingdom.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/46px-Flag_of_the_United_Kingdom.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="512" data-file-width="512" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/16px-Flag_of_Switzerland_%28Pantone%29.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/24px-Flag_of_Switzerland_%28Pantone%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/32px-Flag_of_Switzerland_%28Pantone%29.svg.png 2x" width="16"/></span></span>  </span><a href="/wiki/Switzerland" title="Switzerland">Switzerland</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">4
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/35px-Flag_of_Japan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/45px-Flag_of_Japan.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Japan" title="Japan">Japan</a></td>
<td>2
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Netherlands" title="Netherlands">Netherlands</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/South_Korea" title="South Korea">South Korea</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/35px-Flag_of_France.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/45px-Flag_of_France.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/France" title="France">France</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/35px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/45px-Flag_of_Russia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Russia" title="Russia">Russia</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/23px-Flag_of_Saudi_Arabia.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/35px-Flag_of_Saudi_Arabia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/45px-Flag_of_Saudi_Arabia.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Saudi_Arabia" title="Saudi Arabia">Saudi Arabia</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Singapore" title="Singapore">Singapore</a></td>
<td>1
</td></tr>
<tr>
<th scope="row">5
</th>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><span><img alt="" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/></span></span> </span><a href="/wiki/Taiwan" title="Taiwan">Taiwan</a></td>
<td>1
</td></tr></tbody></table>, <table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th class="navbox-title" colspan="2" scope="col"><link href="mw-data:TemplateStyles:r1129693374" rel="mw-deduplicated-inline-style"/><style data-mw-deduplicate="TemplateStyles:r1063604349">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:Wealth" title="Template:Wealth"><abbr title="View this template">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Wealth" title="Template talk:Wealth"><abbr title="Discuss this template">t</abbr></a></li><li class="nv-edit"><a href="/wiki/Special:EditPage/Template:Wealth" title="Special:EditPage/Template:Wealth"><abbr title="Edit this template">e</abbr></a></li></ul></div><div id="Extreme_wealth" style="font-size:114%;margin:0 4em">Extreme <a href="/wiki/Wealth" title="Wealth">wealth</a></div></th></tr><tr><th class="navbox-group" scope="row" style="width:1%">Concepts</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Capital_accumulation" title="Capital accumulation">Capital accumulation</a>
<ul><li><a href="/wiki/Overaccumulation" title="Overaccumulation">Overaccumulation</a></li></ul></li>
<li><a href="/wiki/Economic_inequality" title="Economic inequality">Economic inequality</a>
<ul><li><a class="mw-redirect" href="/wiki/Wealth_distribution" title="Wealth distribution">Wealth distribution</a></li>
<li><a href="/wiki/Income_distribution" title="Income distribution">Income distribution</a></li>
<li><a href="/wiki/Consumption_distribution" title="Consumption distribution">Consumption distribution</a></li>
<li><a href="/wiki/History_of_economic_inequality" title="History of economic inequality">History of economic inequality</a></li></ul></li>
<li><a href="/wiki/International_inequality" title="International inequality">International inequality</a></li>
<li><a href="/wiki/Elite" title="Elite">Elite</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarchy</a></li>
<li><a href="/wiki/Overclass" title="Overclass">Overclass</a></li>
<li><a href="/wiki/Plutocracy" title="Plutocracy">Plutocracy</a></li>
<li><a href="/wiki/Plutonomy" title="Plutonomy">Plutonomy</a>
<ul><li><ul><li><a href="/wiki/Primitive_accumulation_of_capital" title="Primitive accumulation of capital">Primitive accumulation of capital</a></li></ul></li></ul></li>
<li><a href="/wiki/Upper_class" title="Upper class">Upper class</a>
<ul><li><a href="/wiki/Nouveau_riche" title="Nouveau riche"><i>Nouveau riche</i> <wbr/>(new money)</a></li>
<li><a href="/wiki/Old_money" title="Old money"><i>Vieux riche</i> <wbr/>(old money)</a></li></ul></li>
<li><a class="mw-redirect" href="/wiki/Luxury_good" title="Luxury good">Luxury goods</a>
<ul><li><a href="/wiki/Veblen_good" title="Veblen good">Veblen goods</a>
<ul><li><a href="/wiki/Conspicuous_consumption" title="Conspicuous consumption">Conspicuous consumption</a></li>
<li><a href="/wiki/Conspicuous_leisure" title="Conspicuous leisure">Conspicuous leisure</a></li></ul></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">People</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Billionaire" title="Billionaire">Billionaire</a></li>
<li><a href="/wiki/Captain_of_industry" title="Captain of industry">Captain of industry</a></li>
<li><a href="/wiki/High-net-worth_individual" title="High-net-worth individual">High-net-worth individual</a>
<ul><li><a class="mw-redirect" href="/wiki/Ultra_high-net-worth_individual" title="Ultra high-net-worth individual">UHNWI</a></li></ul></li>
<li><a href="/wiki/Magnate" title="Magnate">Magnate</a>
<ul><li><a href="/wiki/Business_magnate" title="Business magnate">Business</a></li></ul></li>
<li><a href="/wiki/Millionaire" title="Millionaire">Millionaire</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarch</a>
<ul><li><a href="/wiki/Business_oligarch" title="Business oligarch">Business</a></li>
<li><a href="/wiki/Russian_oligarchs" title="Russian oligarchs">Russian</a></li>
<li><a href="/wiki/Ukrainian_oligarchs" title="Ukrainian oligarchs">Ukrainian</a></li></ul></li>
<li><a href="/wiki/Robber_baron_(industrialist)" title="Robber baron (industrialist)">Robber baron</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-redirect" href="/wiki/Wealth_concentration" title="Wealth concentration">Concentration</a></li>
<li><a href="/wiki/Distribution_of_wealth" title="Distribution of wealth">Distribution</a></li>
<li><a class="mw-redirect" href="/wiki/Dynastic_wealth" title="Dynastic wealth">Dynastic</a></li>
<li><a href="/wiki/Wealth_effect" title="Wealth effect">Effect</a></li>
<li><a href="/wiki/Geography_and_wealth" title="Geography and wealth">Geography</a></li>
<li><a href="/wiki/Inheritance" title="Inheritance">Inherited</a></li>
<li><a href="/wiki/Wealth_management" title="Wealth management">Management</a></li>
<li><a class="mw-redirect" href="/wiki/National_wealth" title="National wealth">National</a></li>
<li><a href="/wiki/Paper_wealth" title="Paper wealth">Paper</a></li>
<li><a href="/wiki/Wealth_and_religion" title="Wealth and religion">Religion</a></li>
<li><a href="/wiki/Wealth_tax" title="Wealth tax">Tax</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Lists</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_World%27s_Billionaires" title="The World's Billionaires"><i>Forbes</i> list of billionaires</a></li>
<li><a href="/wiki/List_of_centibillionaires" title="List of centibillionaires">List of centibillionaires</a></li>
<li><a href="/wiki/List_of_female_billionaires" title="List of female billionaires">Female billionaires</a></li>
<li><a href="/wiki/List_of_royalty_by_net_worth" title="List of royalty by net worth">Richest royals</a></li>
<li><a href="/wiki/List_of_richest_Americans_in_history" title="List of richest Americans in history">Wealthiest Americans</a></li>
<li><a href="/wiki/List_of_wealthiest_families" title="List of wealthiest families">Wealthiest families</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-selflink selflink">Largest companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_corporate_profits_and_losses" title="List of largest corporate profits and losses">Largest corporate profits and losses</a></li>
<li><a href="/wiki/List_of_public_corporations_by_market_capitalization" title="List of public corporations by market capitalization">Largest corporations by market capitalization</a></li>
<li><a href="/wiki/List_of_largest_financial_services_companies_by_revenue" title="List of largest financial services companies by revenue">Largest financial services companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_manufacturing_companies_by_revenue" title="List of largest manufacturing companies by revenue">Largest manufacturing companies by revenue</a></li>
<li><a href="/wiki/List_of_the_largest_software_companies" title="List of the largest software companies">Largest software companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_technology_companies_by_revenue" title="List of largest technology companies by revenue">Largest technology companies by revenue</a></li>
<li><a href="/wiki/List_of_wealthiest_charitable_foundations" title="List of wealthiest charitable foundations">Charities</a>
<ul><li><a href="/wiki/List_of_philanthropists" title="List of philanthropists">Philanthropists</a></li></ul></li>
<li>Universities
<ul><li><a href="/wiki/Lists_of_institutions_of_higher_education_by_endowment_size" title="Lists of institutions of higher education by endowment size">Endowment size</a></li>
<li><a href="/wiki/List_of_universities_by_number_of_billionaire_alumni" title="List of universities by number of billionaire alumni">Number of billionaire alumni</a></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Other</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/List_of_cities_by_number_of_billionaires" title="List of cities by number of billionaires">Cities by number of billionaires</a></li>
<li><a class="mw-redirect" href="/wiki/List_of_countries_by_the_number_of_billionaires" title="List of countries by the number of billionaires">Countries by number of billionaires</a></li>
<li><a href="/wiki/List_of_countries_by_total_wealth" title="List of countries by total wealth">Countries by total wealth</a></li>
<li><a href="/wiki/List_of_sovereign_states_by_wealth_inequality" title="List of sovereign states by wealth inequality">Countries by wealth inequality</a></li>
<li><a href="/wiki/Wealth_inequality_in_the_United_States" title="Wealth inequality in the United States">Wealth inequality in the United States</a></li>
<li><a href="/wiki/Income_inequality_in_the_United_States" title="Income inequality in the United States">Income inequality in the United States</a></li>
<li><a href="/wiki/Lists_of_most_expensive_items_by_category" title="Lists of most expensive items by category">Most expensive items</a>
<ul><li><a href="/wiki/Category:Lists_of_most_expensive_things" title="Category:Lists of most expensive things">by category</a></li></ul></li>
<li><a href="/wiki/List_of_wealthiest_animals" title="List of wealthiest animals">Wealthiest animals</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Related</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"></div><table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Diseases_of_affluence" title="Diseases of affluence">Diseases of affluence</a>
<ul><li><a href="/wiki/Affluenza" title="Affluenza">Affluenza</a></li>
<li><a href="/wiki/Narcissism#Celebrity_narcissism" title="Narcissism">Acquired situational narcissism</a></li></ul></li>
<li><i><a href="/wiki/Argumentum_ad_crumenam" title="Argumentum ad crumenam">Argumentum ad crumenam</a></i></li>
<li><a href="/wiki/Prosperity_theology" title="Prosperity theology">Prosperity theology</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_Gospel_of_Wealth" title="The Gospel of Wealth">Gospel of Wealth</a></li>
<li><a href="/wiki/The_Giving_Pledge" title="The Giving Pledge">The Giving Pledge</a></li>
<li><a href="/wiki/Philanthrocapitalism" title="Philanthrocapitalism">Philanthrocapitalism</a></li>
<li><a href="/wiki/Venture_philanthropy" title="Venture philanthropy">Venture philanthropy</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Sayings</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_rich_get_richer_and_the_poor_get_poorer" title="The rich get richer and the poor get poorer">The rich get richer and the poor get poorer</a></li>
<li><a href="/wiki/Socialism_for_the_rich_and_capitalism_for_the_poor" title="Socialism for the rich and capitalism for the poor">Socialism for the rich and capitalism for the poor</a></li>
<li><a href="/wiki/Too_big_to_fail" title="Too big to fail">Too big to fail</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Media</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><i><a href="/wiki/Das_Kapital" title="Das Kapital">Das Kapital</a></i></li>
<li><a href="/wiki/Plutus_(play)" title="Plutus (play)"><i>Plutus</i></a>
<ul><li><a href="/wiki/Plutus" title="Plutus">Greek god of wealth</a></li></ul></li>
<li><a href="/wiki/Superclass_(book)" title="Superclass (book)"><i>Superclass</i></a>
<ul><li><a href="/wiki/The_Superclass_List" title="The Superclass List">List</a></li></ul></li>
<li><i><a href="/wiki/The_Theory_of_the_Leisure_Class" title="The Theory of the Leisure Class">The Theory of the Leisure Class</a></i></li>
<li><a href="/wiki/Wealth_(film)" title="Wealth (film)"><i>Wealth</i></a></li>
<li><i><a href="/wiki/The_Wealth_of_Nations" title="The Wealth of Nations">The Wealth of Nations</a></i></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><td class="navbox-abovebelow" colspan="2"><div>
<ul><li><a href="/wiki/Category:Wealth" title="Category:Wealth">Category</a>
<ul><li><a href="/wiki/Category:Wealth_by_country" title="Category:Wealth by country">by country</a></li></ul></li></ul>
</div></td></tr></tbody></table>, <table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Capital_accumulation" title="Capital accumulation">Capital accumulation</a>
<ul><li><a href="/wiki/Overaccumulation" title="Overaccumulation">Overaccumulation</a></li></ul></li>
<li><a href="/wiki/Economic_inequality" title="Economic inequality">Economic inequality</a>
<ul><li><a class="mw-redirect" href="/wiki/Wealth_distribution" title="Wealth distribution">Wealth distribution</a></li>
<li><a href="/wiki/Income_distribution" title="Income distribution">Income distribution</a></li>
<li><a href="/wiki/Consumption_distribution" title="Consumption distribution">Consumption distribution</a></li>
<li><a href="/wiki/History_of_economic_inequality" title="History of economic inequality">History of economic inequality</a></li></ul></li>
<li><a href="/wiki/International_inequality" title="International inequality">International inequality</a></li>
<li><a href="/wiki/Elite" title="Elite">Elite</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarchy</a></li>
<li><a href="/wiki/Overclass" title="Overclass">Overclass</a></li>
<li><a href="/wiki/Plutocracy" title="Plutocracy">Plutocracy</a></li>
<li><a href="/wiki/Plutonomy" title="Plutonomy">Plutonomy</a>
<ul><li><ul><li><a href="/wiki/Primitive_accumulation_of_capital" title="Primitive accumulation of capital">Primitive accumulation of capital</a></li></ul></li></ul></li>
<li><a href="/wiki/Upper_class" title="Upper class">Upper class</a>
<ul><li><a href="/wiki/Nouveau_riche" title="Nouveau riche"><i>Nouveau riche</i> <wbr/>(new money)</a></li>
<li><a href="/wiki/Old_money" title="Old money"><i>Vieux riche</i> <wbr/>(old money)</a></li></ul></li>
<li><a class="mw-redirect" href="/wiki/Luxury_good" title="Luxury good">Luxury goods</a>
<ul><li><a href="/wiki/Veblen_good" title="Veblen good">Veblen goods</a>
<ul><li><a href="/wiki/Conspicuous_consumption" title="Conspicuous consumption">Conspicuous consumption</a></li>
<li><a href="/wiki/Conspicuous_leisure" title="Conspicuous leisure">Conspicuous leisure</a></li></ul></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">People</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Billionaire" title="Billionaire">Billionaire</a></li>
<li><a href="/wiki/Captain_of_industry" title="Captain of industry">Captain of industry</a></li>
<li><a href="/wiki/High-net-worth_individual" title="High-net-worth individual">High-net-worth individual</a>
<ul><li><a class="mw-redirect" href="/wiki/Ultra_high-net-worth_individual" title="Ultra high-net-worth individual">UHNWI</a></li></ul></li>
<li><a href="/wiki/Magnate" title="Magnate">Magnate</a>
<ul><li><a href="/wiki/Business_magnate" title="Business magnate">Business</a></li></ul></li>
<li><a href="/wiki/Millionaire" title="Millionaire">Millionaire</a></li>
<li><a href="/wiki/Oligarchy" title="Oligarchy">Oligarch</a>
<ul><li><a href="/wiki/Business_oligarch" title="Business oligarch">Business</a></li>
<li><a href="/wiki/Russian_oligarchs" title="Russian oligarchs">Russian</a></li>
<li><a href="/wiki/Ukrainian_oligarchs" title="Ukrainian oligarchs">Ukrainian</a></li></ul></li>
<li><a href="/wiki/Robber_baron_(industrialist)" title="Robber baron (industrialist)">Robber baron</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-redirect" href="/wiki/Wealth_concentration" title="Wealth concentration">Concentration</a></li>
<li><a href="/wiki/Distribution_of_wealth" title="Distribution of wealth">Distribution</a></li>
<li><a class="mw-redirect" href="/wiki/Dynastic_wealth" title="Dynastic wealth">Dynastic</a></li>
<li><a href="/wiki/Wealth_effect" title="Wealth effect">Effect</a></li>
<li><a href="/wiki/Geography_and_wealth" title="Geography and wealth">Geography</a></li>
<li><a href="/wiki/Inheritance" title="Inheritance">Inherited</a></li>
<li><a href="/wiki/Wealth_management" title="Wealth management">Management</a></li>
<li><a class="mw-redirect" href="/wiki/National_wealth" title="National wealth">National</a></li>
<li><a href="/wiki/Paper_wealth" title="Paper wealth">Paper</a></li>
<li><a href="/wiki/Wealth_and_religion" title="Wealth and religion">Religion</a></li>
<li><a href="/wiki/Wealth_tax" title="Wealth tax">Tax</a></li></ul>
</div></td></tr></tbody></table>, <table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_World%27s_Billionaires" title="The World's Billionaires"><i>Forbes</i> list of billionaires</a></li>
<li><a href="/wiki/List_of_centibillionaires" title="List of centibillionaires">List of centibillionaires</a></li>
<li><a href="/wiki/List_of_female_billionaires" title="List of female billionaires">Female billionaires</a></li>
<li><a href="/wiki/List_of_royalty_by_net_worth" title="List of royalty by net worth">Richest royals</a></li>
<li><a href="/wiki/List_of_richest_Americans_in_history" title="List of richest Americans in history">Wealthiest Americans</a></li>
<li><a href="/wiki/List_of_wealthiest_families" title="List of wealthiest families">Wealthiest families</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a class="mw-selflink selflink">Largest companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_corporate_profits_and_losses" title="List of largest corporate profits and losses">Largest corporate profits and losses</a></li>
<li><a href="/wiki/List_of_public_corporations_by_market_capitalization" title="List of public corporations by market capitalization">Largest corporations by market capitalization</a></li>
<li><a href="/wiki/List_of_largest_financial_services_companies_by_revenue" title="List of largest financial services companies by revenue">Largest financial services companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_manufacturing_companies_by_revenue" title="List of largest manufacturing companies by revenue">Largest manufacturing companies by revenue</a></li>
<li><a href="/wiki/List_of_the_largest_software_companies" title="List of the largest software companies">Largest software companies by revenue</a></li>
<li><a href="/wiki/List_of_largest_technology_companies_by_revenue" title="List of largest technology companies by revenue">Largest technology companies by revenue</a></li>
<li><a href="/wiki/List_of_wealthiest_charitable_foundations" title="List of wealthiest charitable foundations">Charities</a>
<ul><li><a href="/wiki/List_of_philanthropists" title="List of philanthropists">Philanthropists</a></li></ul></li>
<li>Universities
<ul><li><a href="/wiki/Lists_of_institutions_of_higher_education_by_endowment_size" title="Lists of institutions of higher education by endowment size">Endowment size</a></li>
<li><a href="/wiki/List_of_universities_by_number_of_billionaire_alumni" title="List of universities by number of billionaire alumni">Number of billionaire alumni</a></li></ul></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Other</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/List_of_cities_by_number_of_billionaires" title="List of cities by number of billionaires">Cities by number of billionaires</a></li>
<li><a class="mw-redirect" href="/wiki/List_of_countries_by_the_number_of_billionaires" title="List of countries by the number of billionaires">Countries by number of billionaires</a></li>
<li><a href="/wiki/List_of_countries_by_total_wealth" title="List of countries by total wealth">Countries by total wealth</a></li>
<li><a href="/wiki/List_of_sovereign_states_by_wealth_inequality" title="List of sovereign states by wealth inequality">Countries by wealth inequality</a></li>
<li><a href="/wiki/Wealth_inequality_in_the_United_States" title="Wealth inequality in the United States">Wealth inequality in the United States</a></li>
<li><a href="/wiki/Income_inequality_in_the_United_States" title="Income inequality in the United States">Income inequality in the United States</a></li>
<li><a href="/wiki/Lists_of_most_expensive_items_by_category" title="Lists of most expensive items by category">Most expensive items</a>
<ul><li><a href="/wiki/Category:Lists_of_most_expensive_things" title="Category:Lists of most expensive things">by category</a></li></ul></li>
<li><a href="/wiki/List_of_wealthiest_animals" title="List of wealthiest animals">Wealthiest animals</a></li></ul>
</div></td></tr></tbody></table>, <table class="nowraplinks navbox-subgroup" style="border-spacing:0"><tbody><tr><td class="navbox-list navbox-odd" colspan="2" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Diseases_of_affluence" title="Diseases of affluence">Diseases of affluence</a>
<ul><li><a href="/wiki/Affluenza" title="Affluenza">Affluenza</a></li>
<li><a href="/wiki/Narcissism#Celebrity_narcissism" title="Narcissism">Acquired situational narcissism</a></li></ul></li>
<li><i><a href="/wiki/Argumentum_ad_crumenam" title="Argumentum ad crumenam">Argumentum ad crumenam</a></i></li>
<li><a href="/wiki/Prosperity_theology" title="Prosperity theology">Prosperity theology</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_Gospel_of_Wealth" title="The Gospel of Wealth">Gospel of Wealth</a></li>
<li><a href="/wiki/The_Giving_Pledge" title="The Giving Pledge">The Giving Pledge</a></li>
<li><a href="/wiki/Philanthrocapitalism" title="Philanthrocapitalism">Philanthrocapitalism</a></li>
<li><a href="/wiki/Venture_philanthropy" title="Venture philanthropy">Venture philanthropy</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Sayings</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/The_rich_get_richer_and_the_poor_get_poorer" title="The rich get richer and the poor get poorer">The rich get richer and the poor get poorer</a></li>
<li><a href="/wiki/Socialism_for_the_rich_and_capitalism_for_the_poor" title="Socialism for the rich and capitalism for the poor">Socialism for the rich and capitalism for the poor</a></li>
<li><a href="/wiki/Too_big_to_fail" title="Too big to fail">Too big to fail</a></li></ul>
</div></td></tr><tr><th class="navbox-group" scope="row" style="width:1%">Media</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><i><a href="/wiki/Das_Kapital" title="Das Kapital">Das Kapital</a></i></li>
<li><a href="/wiki/Plutus_(play)" title="Plutus (play)"><i>Plutus</i></a>
<ul><li><a href="/wiki/Plutus" title="Plutus">Greek god of wealth</a></li></ul></li>
<li><a href="/wiki/Superclass_(book)" title="Superclass (book)"><i>Superclass</i></a>
<ul><li><a href="/wiki/The_Superclass_List" title="The Superclass List">List</a></li></ul></li>
<li><i><a href="/wiki/The_Theory_of_the_Leisure_Class" title="The Theory of the Leisure Class">The Theory of the Leisure Class</a></i></li>
<li><a href="/wiki/Wealth_(film)" title="Wealth (film)"><i>Wealth</i></a></li>
<li><i><a href="/wiki/The_Wealth_of_Nations" title="The Wealth of Nations">The Wealth of Nations</a></i></li></ul>
</div></td></tr></tbody></table>]
soup.find_all('th')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
[<th rowspan="2" scope="col">Rank
</th>, <th rowspan="2" scope="col">Name
</th>, <th rowspan="2" scope="col">Industry
</th>, <th scope="col">Revenue
</th>, <th scope="col">Profit
</th>, <th rowspan="2" scope="col">Employees
</th>, <th rowspan="2" scope="col">Headquarters<sup class="reference" id="cite_ref-4"><a href="#cite_note-4">[note 1]</a></sup>
</th>, <th rowspan="2" scope="col"><a href="/wiki/State-owned_enterprise" title="State-owned enterprise">State-owned</a>
</th>, <th class="unsortable" rowspan="2" scope="col"><abbr title="Reference(s)">Ref.</abbr>
</th>, <th rowspan="2" scope="col">Revenue per worker
</th>, <th colspan="2" scope="col"><small>USD millions</small>
</th>, <th scope="col">1
</th>, <th scope="row">2
</th>, <th scope="row">3
</th>, <th scope="row">4
</th>, <th scope="row">5
</th>, <th scope="row">6
</th>, <th scope="row">7
</th>, <th scope="row">8
</th>, <th scope="row">9
</th>, <th scope="row">10
</th>, <th scope="row">11
</th>, <th scope="row">12
</th>, <th scope="row">13
</th>, <th scope="row">14
</th>, <th scope="row">15
</th>, <th scope="row">16
</th>, <th scope="row">17
</th>, <th scope="row">18
</th>, <th scope="row">19
</th>, <th scope="row">20
</th>, <th scope="row">21
</th>, <th scope="row">22
</th>, <th scope="row">23
</th>, <th scope="row">24
</th>, <th scope="row">25
</th>, <th scope="row">26
</th>, <th scope="row">27
</th>, <th scope="row">28
</th>, <th scope="row">29
</th>, <th scope="row">30
</th>, <th scope="row">31
</th>, <th>32
</th>, <th scope="row">33
</th>, <th scope="row">34
</th>, <th scope="row">35
</th>, <th>36
</th>, <th scope="row">37
</th>, <th scope="row">38
</th>, <th>39
</th>, <th scope="row">40
</th>, <th scope="row">41
</th>, <th scope="row">42
</th>, <th scope="row">43
</th>, <th scope="row">44
</th>, <th scope="row">45
</th>, <th scope="row">46
</th>, <th scope="row">47
</th>, <th>48
</th>, <th scope="row">49
</th>, <th scope="row">50
</th>, <th scope="col">Rank
</th>, <th scope="col">Country
</th>, <th scope="col">Companies
</th>, <th scope="row">1
</th>, <th scope="row">2
</th>, <th scope="row">3
</th>, <th scope="row">4
</th>, <th scope="row">4
</th>, <th scope="row">4
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th class="navbox-title" colspan="2" scope="col"><link href="mw-data:TemplateStyles:r1129693374" rel="mw-deduplicated-inline-style"/><style data-mw-deduplicate="TemplateStyles:r1063604349">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:Wealth" title="Template:Wealth"><abbr title="View this template">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Wealth" title="Template talk:Wealth"><abbr title="Discuss this template">t</abbr></a></li><li class="nv-edit"><a href="/wiki/Special:EditPage/Template:Wealth" title="Special:EditPage/Template:Wealth"><abbr title="Edit this template">e</abbr></a></li></ul></div><div id="Extreme_wealth" style="font-size:114%;margin:0 4em">Extreme <a href="/wiki/Wealth" title="Wealth">wealth</a></div></th>, <th class="navbox-group" scope="row" style="width:1%">Concepts</th>, <th class="navbox-group" scope="row" style="width:1%">People</th>, <th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th>, <th class="navbox-group" scope="row" style="width:1%">Lists</th>, <th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th>, <th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th>, <th class="navbox-group" scope="row" style="width:1%">Other</th>, <th class="navbox-group" scope="row" style="width:1%">Related</th>, <th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th>, <th class="navbox-group" scope="row" style="width:1%">Sayings</th>, <th class="navbox-group" scope="row" style="width:1%">Media</th>]
world_titles=soup.find_all('th')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
world_titles
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
[<th rowspan="2" scope="col">Rank
</th>, <th rowspan="2" scope="col">Name
</th>, <th rowspan="2" scope="col">Industry
</th>, <th scope="col">Revenue
</th>, <th scope="col">Profit
</th>, <th rowspan="2" scope="col">Employees
</th>, <th rowspan="2" scope="col">Headquarters<sup class="reference" id="cite_ref-4"><a href="#cite_note-4">[note 1]</a></sup>
</th>, <th rowspan="2" scope="col"><a href="/wiki/State-owned_enterprise" title="State-owned enterprise">State-owned</a>
</th>, <th class="unsortable" rowspan="2" scope="col"><abbr title="Reference(s)">Ref.</abbr>
</th>, <th rowspan="2" scope="col">Revenue per worker
</th>, <th colspan="2" scope="col"><small>USD millions</small>
</th>, <th scope="col">1
</th>, <th scope="row">2
</th>, <th scope="row">3
</th>, <th scope="row">4
</th>, <th scope="row">5
</th>, <th scope="row">6
</th>, <th scope="row">7
</th>, <th scope="row">8
</th>, <th scope="row">9
</th>, <th scope="row">10
</th>, <th scope="row">11
</th>, <th scope="row">12
</th>, <th scope="row">13
</th>, <th scope="row">14
</th>, <th scope="row">15
</th>, <th scope="row">16
</th>, <th scope="row">17
</th>, <th scope="row">18
</th>, <th scope="row">19
</th>, <th scope="row">20
</th>, <th scope="row">21
</th>, <th scope="row">22
</th>, <th scope="row">23
</th>, <th scope="row">24
</th>, <th scope="row">25
</th>, <th scope="row">26
</th>, <th scope="row">27
</th>, <th scope="row">28
</th>, <th scope="row">29
</th>, <th scope="row">30
</th>, <th scope="row">31
</th>, <th>32
</th>, <th scope="row">33
</th>, <th scope="row">34
</th>, <th scope="row">35
</th>, <th>36
</th>, <th scope="row">37
</th>, <th scope="row">38
</th>, <th>39
</th>, <th scope="row">40
</th>, <th scope="row">41
</th>, <th scope="row">42
</th>, <th scope="row">43
</th>, <th scope="row">44
</th>, <th scope="row">45
</th>, <th scope="row">46
</th>, <th scope="row">47
</th>, <th>48
</th>, <th scope="row">49
</th>, <th scope="row">50
</th>, <th scope="col">Rank
</th>, <th scope="col">Country
</th>, <th scope="col">Companies
</th>, <th scope="row">1
</th>, <th scope="row">2
</th>, <th scope="row">3
</th>, <th scope="row">4
</th>, <th scope="row">4
</th>, <th scope="row">4
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th scope="row">5
</th>, <th class="navbox-title" colspan="2" scope="col"><link href="mw-data:TemplateStyles:r1129693374" rel="mw-deduplicated-inline-style"/><style data-mw-deduplicate="TemplateStyles:r1063604349">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:Wealth" title="Template:Wealth"><abbr title="View this template">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Wealth" title="Template talk:Wealth"><abbr title="Discuss this template">t</abbr></a></li><li class="nv-edit"><a href="/wiki/Special:EditPage/Template:Wealth" title="Special:EditPage/Template:Wealth"><abbr title="Edit this template">e</abbr></a></li></ul></div><div id="Extreme_wealth" style="font-size:114%;margin:0 4em">Extreme <a href="/wiki/Wealth" title="Wealth">wealth</a></div></th>, <th class="navbox-group" scope="row" style="width:1%">Concepts</th>, <th class="navbox-group" scope="row" style="width:1%">People</th>, <th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Wealth" title="Wealth">Wealth</a></th>, <th class="navbox-group" scope="row" style="width:1%">Lists</th>, <th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Lists_of_people_by_net_worth" title="Lists of people by net worth">People</a></th>, <th class="navbox-group" scope="row" style="width:1%"><a class="mw-redirect" href="/wiki/List_of_wealthiest_organizations" title="List of wealthiest organizations">Organizations</a></th>, <th class="navbox-group" scope="row" style="width:1%">Other</th>, <th class="navbox-group" scope="row" style="width:1%">Related</th>, <th class="navbox-group" scope="row" style="width:1%"><a href="/wiki/Philanthropy" title="Philanthropy">Philanthropy</a></th>, <th class="navbox-group" scope="row" style="width:1%">Sayings</th>, <th class="navbox-group" scope="row" style="width:1%">Media</th>]
world_table_titles=[titles.text.strip() for titles in world_titles]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
print(world_table_titles)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
['Rank', 'Name', 'Industry', 'Revenue', 'Profit', 'Employees', 'Headquarters[note 1]', 'State-owned', 'Ref.', 'Revenue per worker', 'USD millions', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', 'Rank', 'Country', 'Companies', '1', '2', '3', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', 'vteExtreme wealth', 'Concepts', 'People', 'Wealth', 'Lists', 'People', 'Organizations', 'Other', 'Related', 'Philanthropy', 'Sayings', 'Media']
import pandas as pd
df=
df=pd.DataFrame(columns=world_table_titles)
df
Empty DataFrame
Columns: [Rank, Name, Industry, Revenue, Profit, Employees, Headquarters[note 1], State-owned, Ref., Revenue per worker, USD millions, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, Rank, Country, Companies, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, vteExtreme wealth, Concepts, People, Wealth, Lists, People, Organizations, Other, Related, Philanthropy, Sayings, Media]
Index: []

[0 rows x 89 columns]
column_data=soup.find_all('tr')
for row in column-data[2:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    for row in column_data[2:]:
        column_data=soup.find_all('tr')
        for row in column_data[2:]:
            row_data = row.find_all('td')
            individual_row_data= [data.text.strip() for data in row_data]
            print(individual_row_data)

            
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    for row in column-data[2:]:
NameError: name 'column' is not defined
column_data=soup.find_all('tr')
for row in column_data[2:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

    
['Walmart', 'Retail', '$611,289', '$11,680', '2,100,000', 'United States', '', '[1]', '$291,090.00']
['Saudi Aramco', 'Oil and gas', '$603,651', '$159,069', '70,496', 'Saudi Arabia', '', '[4]', '$8,562,911.37']
['Amazon', 'Retail', '$574,785', '$30,425', '1,525,000', 'United States', '', '[5]', '$376,908.20']
['State Grid Corporation of China', 'Electricity', '$530,009', '$8,192', '870,287', 'China', '', '[6]', '$609,004.85']
['Vitol', 'Commodities', '$505,000', '$15,000', '1,560', 'Switzerland', '', '[7][8]', '$323,717,948.72']
['China National Petroleum Corporation', 'Oil and gas', '$483,019', '$21,080', '1,087,049', 'China', '', '[9]', '$444,339.68']
['China Petrochemical Corporation', 'Oil and gas', '$471,154', '$9,657', '527,487', 'China', '', '[10]', '$893,204.95']
['ExxonMobil', 'Oil and gas', '$413,680', '$55,740', '63,000', 'United States', '', '[11]', '$6,566,349.21']
['Apple', 'Electronics', '$394,328', '$99,803', '164,000', 'United States', '', '[12]', '$2,404,439.02']
['Shell', 'Oil and gas', '$386,201', '$20,120', '93,000', 'United Kingdom', '', '[13]', '$4,152,698.92']
['UnitedHealth Group', 'Healthcare', '$324,162', '$20,120', '400,000', 'United States', '', '[14]', '$810,405.00']
['CVS Health', 'Healthcare', '$322,467', '$4,149', '259,500', 'United States', '', '[15]', '$1,242,647.40']
['Trafigura', 'Commodities', '$318,476', '$6,994', '12,347', 'Singapore', '', '[16]', '$25,793,796.06']
['China State Construction Engineering', 'Construction', '$305,885', '$4,234', '382,492', 'China', '', '[17]', '$799,716.07']
['Berkshire Hathaway', 'Financials', '$302,089', '−$22,819', '383,000', 'United States', '', '[18]', '$788,744.13']
['Volkswagen Group', 'Automotive', '$293,685', '$15,233', '675,805', 'Germany', '', '[19]', '$434,570.62']
['Uniper', 'Electricity', '$288,309', '−$19,961', '7,008', 'Germany', '', '[20]', '$41,139,982.88']
['Alphabet', 'Information technology', '$282,836', '$59,972', '190,234', 'United States', '', '[21]', '$1,486,779.44']
['McKesson', 'Healthcare', '$276,711', '$3,560', '48,000', 'United States', '', '[22]', '$5,764,812.50']
['Toyota', 'Automotive', '$274,491', '$18,110', '375,235', 'Japan', '', '[23]', '$731,517.58']
['TotalEnergies', 'Oil and gas', '$263,310', '$20,526', '101,279', 'France', '', '[24]', '$2,599,847.94']
['Glencore', 'Commodities', '$255,984', '$17,320', '81,284', 'Switzerland', '', '[25]', '$3,149,254.47']
['BP', 'Oil and gas', '$248,891', '−$2,487', '67,600', 'United Kingdom', '', '[26]', '$3,681,819.53']
['Chevron', 'Oil and gas', '$246,252', '$35,465', '43,846', 'United States', '', '[27]', '$5,616,293.39']
['Cencora', 'Healthcare', '$238,587', '$1,699', '41,500', 'United States', '', '[28]', '$5,749,084.34']
['Samsung Electronics', 'Electronics', '$234,129', '$42,398', '270,372', 'South Korea', '', '[29]', '$865,951.36']
['Costco', 'Retail', '$226,954', '$5,844', '304,000', 'United States', '', '[30]', '$746,559.21']
['Foxconn', 'Electronics', '$222,535', '$4,751', '767,062', 'Taiwan', '', '[31]', '$290,113.45']
['Industrial and Commercial Bank of China', 'Financials', '$214,766', '$53,589', '427,587', 'China', '', '[32]', '$502,274.39']
['Microsoft', 'Information technology', '$211,915', '$73,307', '221,000', 'United States', '', '[33]', '$897,149.32']
['China Construction Bank', 'Financials', '$202,753', '$48,145', '376,682', 'China', '', '[34]', '$538,260.39']
['Stellantis', 'Automotive', '$188,888', '$17,669', '272,367', 'Netherlands', '', '[35]', '$693,505.45']
['Agricultural Bank of China', 'Financials', '$187,061', '$38,524', '452,258', 'China', '', '[36]', '$413,615.68']
['Ping An Insurance', 'Financials', '$181,566', '$12,454', '344,223', 'China', '', '[37]', '$527,466.21']
['Cardinal Health', 'Healthcare', '$181,364', '−$933', '46,035', 'United States', '', '[38]', '$3,939,698.06']
['Cigna', 'Healthcare', '$180,516', '$6,668', '70,231', 'United States', '', '[39]', '$2,570,317.95']
['Marathon Petroleum', 'Oil and gas', '$180,012', '$14,516', '17,800', 'United States', '', '[40]', '$10,113,033.71']
['Phillips 66', 'Oil and gas', '$175,702', '$11,024', '13,000', 'United States', '', '[41]', '$13,515,538.46']
['Sinochem', 'Chemicals', '$173,834', '–$1', '220,760', 'China', '', '[42]', '$787,434.32']
['China Railway Engineering Corporation', 'Construction', '$171,669', '$2,035', '314,792', 'China', '', '[43]', '$545,341.05']
['Valero Energy', 'Oil and gas', '$171,189', '$11,528', '9,743', 'United States', '', '[44]', '$17,570,460.84']
['Gazprom', 'Oil and gas', '$167,832', '$17,641', '468,000', 'Russia', '', '[45]', '$358,615.38']
['Cargill', 'Conglomerate', '$165,000', '...', '155,000', 'United States', '', '[46]', '$1,064,516.13']
['China National Offshore Oil Corporation', 'Oil and gas', '$164,762', '$16,988', '81,775', 'China', '', '[47]', '$2,014,821.16']
['China Railway Construction Corporation', 'Construction', '$163,037', '$1,800', '342,098', 'China', '', '[48]', '$476,579.81']
['Baowu', 'Steel', '$161,698', '$2,493', '245,675', 'China', '', '[49]', '$658,178.49']
['Schwarz Gruppe', 'Retail', '$159,800', '...', '575,000', 'Germany', '', '[50]', '$277,913.04']
['Mitsubishi Group', 'Conglomerate', '$159,371', '$8,723', '79,706', 'Japan', '', '[51]', '$1,999,485.61']
['Ford Motor Company', 'Automotive', '$158,057', '−$1,981', '173,000', 'United States', '', '[52]', '$913,624.28']
['Mercedes-Benz Group', 'Automotive', '$157,403', '$15,252', '168,797', 'Germany', '', '[53]', '$932,498.80']
[]
['United States of America', '20']
['China', '13']
['Germany', '4']
['United Kingdom', '2']
['Switzerland', '2']
['Japan', '2']
['Netherlands', '1']
['South Korea', '1']
['France', '1']
['Russia', '1']
['Saudi Arabia', '1']
['Singapore', '1']
['Taiwan', '1']
[]
['Capital accumulation\nOveraccumulation\nEconomic inequality\nWealth distribution\nIncome distribution\nConsumption distribution\nHistory of economic inequality\nInternational inequality\nElite\nOligarchy\nOverclass\nPlutocracy\nPlutonomy\nPrimitive accumulation of capital\nUpper class\nNouveau riche (new money)\nVieux riche (old money)\nLuxury goods\nVeblen goods\nConspicuous consumption\nConspicuous leisure\nPeople\nBillionaire\nCaptain of industry\nHigh-net-worth individual\nUHNWI\nMagnate\nBusiness\nMillionaire\nOligarch\nBusiness\nRussian\nUkrainian\nRobber baron\nWealth\nConcentration\nDistribution\nDynastic\nEffect\nGeography\nInherited\nManagement\nNational\nPaper\nReligion\nTax', 'Capital accumulation\nOveraccumulation\nEconomic inequality\nWealth distribution\nIncome distribution\nConsumption distribution\nHistory of economic inequality\nInternational inequality\nElite\nOligarchy\nOverclass\nPlutocracy\nPlutonomy\nPrimitive accumulation of capital\nUpper class\nNouveau riche (new money)\nVieux riche (old money)\nLuxury goods\nVeblen goods\nConspicuous consumption\nConspicuous leisure', 'Billionaire\nCaptain of industry\nHigh-net-worth individual\nUHNWI\nMagnate\nBusiness\nMillionaire\nOligarch\nBusiness\nRussian\nUkrainian\nRobber baron', 'Concentration\nDistribution\nDynastic\nEffect\nGeography\nInherited\nManagement\nNational\nPaper\nReligion\nTax']
['Capital accumulation\nOveraccumulation\nEconomic inequality\nWealth distribution\nIncome distribution\nConsumption distribution\nHistory of economic inequality\nInternational inequality\nElite\nOligarchy\nOverclass\nPlutocracy\nPlutonomy\nPrimitive accumulation of capital\nUpper class\nNouveau riche (new money)\nVieux riche (old money)\nLuxury goods\nVeblen goods\nConspicuous consumption\nConspicuous leisure']
['Billionaire\nCaptain of industry\nHigh-net-worth individual\nUHNWI\nMagnate\nBusiness\nMillionaire\nOligarch\nBusiness\nRussian\nUkrainian\nRobber baron']
['Concentration\nDistribution\nDynastic\nEffect\nGeography\nInherited\nManagement\nNational\nPaper\nReligion\nTax']
['People\nForbes list of billionaires\nList of centibillionaires\nFemale billionaires\nRichest royals\nWealthiest Americans\nWealthiest families\nOrganizations\nLargest companies by revenue\nLargest corporate profits and losses\nLargest corporations by market capitalization\nLargest financial services companies by revenue\nLargest manufacturing companies by revenue\nLargest software companies by revenue\nLargest technology companies by revenue\nCharities\nPhilanthropists\nUniversities\nEndowment size\nNumber of billionaire alumni\nOther\nCities by number of billionaires\nCountries by number of billionaires\nCountries by total wealth\nCountries by wealth inequality\nWealth inequality in the United States\nIncome inequality in the United States\nMost expensive items\nby category\nWealthiest animals', 'Forbes list of billionaires\nList of centibillionaires\nFemale billionaires\nRichest royals\nWealthiest Americans\nWealthiest families', 'Largest companies by revenue\nLargest corporate profits and losses\nLargest corporations by market capitalization\nLargest financial services companies by revenue\nLargest manufacturing companies by revenue\nLargest software companies by revenue\nLargest technology companies by revenue\nCharities\nPhilanthropists\nUniversities\nEndowment size\nNumber of billionaire alumni', 'Cities by number of billionaires\nCountries by number of billionaires\nCountries by total wealth\nCountries by wealth inequality\nWealth inequality in the United States\nIncome inequality in the United States\nMost expensive items\nby category\nWealthiest animals']
['Forbes list of billionaires\nList of centibillionaires\nFemale billionaires\nRichest royals\nWealthiest Americans\nWealthiest families']
['Largest companies by revenue\nLargest corporate profits and losses\nLargest corporations by market capitalization\nLargest financial services companies by revenue\nLargest manufacturing companies by revenue\nLargest software companies by revenue\nLargest technology companies by revenue\nCharities\nPhilanthropists\nUniversities\nEndowment size\nNumber of billionaire alumni']
['Cities by number of billionaires\nCountries by number of billionaires\nCountries by total wealth\nCountries by wealth inequality\nWealth inequality in the United States\nIncome inequality in the United States\nMost expensive items\nby category\nWealthiest animals']
['Diseases of affluence\nAffluenza\nAcquired situational narcissism\nArgumentum ad crumenam\nProsperity theology\nPhilanthropy\nGospel of Wealth\nThe Giving Pledge\nPhilanthrocapitalism\nVenture philanthropy\nSayings\nThe rich get richer and the poor get poorer\nSocialism for the rich and capitalism for the poor\nToo big to fail\nMedia\nDas Kapital\nPlutus\nGreek god of wealth\nSuperclass\nList\nThe Theory of the Leisure Class\nWealth\nThe Wealth of Nations', 'Diseases of affluence\nAffluenza\nAcquired situational narcissism\nArgumentum ad crumenam\nProsperity theology', 'Gospel of Wealth\nThe Giving Pledge\nPhilanthrocapitalism\nVenture philanthropy', 'The rich get richer and the poor get poorer\nSocialism for the rich and capitalism for the poor\nToo big to fail', 'Das Kapital\nPlutus\nGreek god of wealth\nSuperclass\nList\nThe Theory of the Leisure Class\nWealth\nThe Wealth of Nations']
['Diseases of affluence\nAffluenza\nAcquired situational narcissism\nArgumentum ad crumenam\nProsperity theology']
['Gospel of Wealth\nThe Giving Pledge\nPhilanthrocapitalism\nVenture philanthropy']
['The rich get richer and the poor get poorer\nSocialism for the rich and capitalism for the poor\nToo big to fail']
['Das Kapital\nPlutus\nGreek god of wealth\nSuperclass\nList\nThe Theory of the Leisure Class\nWealth\nThe Wealth of Nations']
['Category\nby country']
df=pd.DataFrame(world_table_titles)
df
               0
0           Rank
1           Name
2       Industry
3        Revenue
4         Profit
..           ...
84         Other
85       Related
86  Philanthropy
87       Sayings
88         Media

[89 rows x 1 columns]
