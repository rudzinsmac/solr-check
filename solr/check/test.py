import requests
import xml.etree.ElementTree as ET

solrTypes = [
    'about',
    'answer',
    'affiliate',
    'album',
    'albumPhoto',
    'alert',
    'appConfig',
    'articleList',
    'articleListItem',
    'asset',
    'assetCarousel',
    'avatar',
    'bbStats',
    'bigBrotherLiveAlert',
    'blockNavigation',
    'blog',
    'blogCategory',
    'brand',
    'callout',
    'carousel',
    'carouselTab',
    'cast',
    'castAlliance',
    'castAllianceAffiliationGroup',
    'castAllianceGroup',
    'catchup',
    'cbsAdConfig',
    'cbsAdType',
    'cbsAdTypeAssocKeyValue',
    'cbsConnect',
    'cbsLocalAffiliate',
    'cbsPackage',
    'cbsPackageToken',
    'cbsProduct',
    'cbsProductAddOn',
    'cbsRecommendedHomeShow',
    'cbsRecommendationConfig',
    'cbsRedirect',
    'cbsSweepstakes',
    'cbsSweepstakesPage',
    'channel',
    'channelListing',
    'configuration',
    'connectArchive',
    'connectEvent',
    'contentFeed',
    'content_term',
    'defaultSchedule',
    'defaultScheduleGroup',
    'deviceHome',
    'devicePromo',
    'endCardTestConfig',
    'endCardTestConfigEndpoint',
    'emailTemplate',
    'episode',
    'event',
    'externalHomeShowGroup',
    'externalHomeShowGroupSection',
    'externalHomeShowGroupItem',
    'movieGenre',
    'feature',
    'featureConfig',
    'featuredShow',
    'flashback',
    'game',
    'gameGroup',
    'gamePromo',
    'gamePromoGroup',
    'globalMenu',
    'giveaway',
    'guest',
    'homeMarquee',
    'homePromo',
    'homePromoGroup',
    'homeShowGroup',
    'homeShowGroupSection',
    'homeShowGroupItem',
    'homeSlide',
    'liveEvent',
    'marquee',
    'marqueeGroup',
    'metadata',
    'mobileWebPromotionalMarquee',
    'movie',
    'movieAsset',
    'multiChannelGroup',
    'multiChannelStream',
    'mvpdConfig',
    'mvpdConfigPlatform',
    'navCategory',
    'navItem',
    'navItemLink',
    'nomination',
    'nominationType',
    'page',
    'pageAttribute',
    'photoStream',
    'platformAsset',
    'poll',
    'pollQuestion',
    'pollQuestionAnswer',
    'profile',
    'promo',
    'question',
    'quiz',
    'recommendation',
    'relatedShow',
    'relatedShowMovie',
    'schedule',
    'season',
    'show',
    'showAlert',
    'showMenu',
    'showMenuLink',
    'showAsset',
    'showGroup',
    'showGroupItem',
    'showGroupItemLink',
    'showNominationArtist',
    'showNominationCategory',
    'showNominationNominee',
    'showPage',
    'showPoll',
    'showSchedule',
    'showSeasonAsset',
    'siteMapPhoto',
    'slide',
    'streamItem',
    'surveyQuestion',
    'term',
    'termV1',
    'topTen',
    'tracking',
    'trendingShowOverride',
    'twitterCarousel',
    'upsell',
    'upsellCampaignAvailability',
    'user',
    'uvpConfig',
    'uvpConfigAttribute',
    'videoConfig',
    'videoListicle',
    'videoListicleContent',
    'videoSection',
    'videoSectionCustomSort',
    'vote',
    'voteAnswer',
    'voteQuestion',
    'zipCode'
]

urls = [
    'http://api-solr-gcp.cbs.com:7305/solr/cbs-blog/select',  # US PROD
    'http://cms-solr-slave.intl.paramountplus.com/solr/cbs-blog/select',  # P+ PROD
    'http://cms-solr-slave.stage.intl.paramountplus.com/solr/cbs-blog/select',  # P+ STAGE
]
for url in urls:
    print(url)

print('type,', end='')
for url in urls:
    print('locale,region,fallback,', end='')
print('')
for t in solrTypes:
    print(f'{t},', end='')
    for url in urls:
        params = dict(
            q='type:' + t,
            rows='1'
        )
        resp = requests.get(url=url, params=params)
        data = resp.text
        root = ET.ElementTree(ET.fromstring(data)).getroot()
        exists = root.find('./result/doc') is not None
        region = root.find('./result/doc/str[@name="region"]') is not None
        locale = root.find('./result/doc/str[@name="locale"]') is not None
        fallback = root.find('./result/doc/arr[@name="all_locales"]') is not None
#        if locale or region or fallback:
        if exists:
            print(f'{locale},{region},{fallback},', end='')
        else:
            print(f',,,', end='')
    print('')
