# -*- coding: utf-8 -*-
from datetime import datetime
import scrapy

from ..items import WebPageItem


def get_clean_string(one_element: list):
    """
        Expects a single element list
        Returns the stripped element in the list
    """

    if one_element:
        one_element = one_element.pop()
        one_element = one_element.strip()
    else:
        one_element = None
    return one_element


class CelSpider(scrapy.Spider):
    name = "cel"
    allowed_domains = ["www.cel.ro"]
    start_urls = ['http://www.cel.ro/laptop-laptopuri/',
                  'http://www.cel.ro/laptopuri-reconditionate/',
                  'http://www.cel.ro/laptop-renew/',
                  'http://www.cel.ro/accesorii-laptop/',
                  'http://www.cel.ro/mouse-laptop/',
                  'http://www.cel.ro/genti-laptop/',
                  'http://www.cel.ro/memorii-laptop/',
                  'http://www.cel.ro/extensie-garantie/',
                  'http://www.cel.ro/hard-disk_uri-laptop/',
                  'http://www.cel.ro/unitati-optice-laptop/',
                  'http://www.cel.ro/acumulatori-incarcatoare-laptop/',
                  'http://www.cel.ro/standuri-coolere-laptop/',
                  'http://www.cel.ro/tastaturi-numerice/',
                  'http://www.cel.ro/cabluri-laptop/',
                  'http://www.cel.ro/docking-station/',
                  'http://www.cel.ro/accesorii-diverse/',
                  'http://www.cel.ro/tastaturi-laptop/',
                  'http://www.cel.ro/tablete/',
                  'http://www.cel.ro/accesorii-tablete/',
                  'http://www.cel.ro/cablu/',
                  'http://www.cel.ro/huse-tablete/',
                  'http://www.cel.ro/incarcator/',
                  'http://www.cel.ro/dock/',
                  'http://www.cel.ro/keyboard-dock/',
                  'http://www.cel.ro/accesorii-diverse-tablete/',
                  'http://www.cel.ro/folii-protectie-tablete/',
                  'http://www.cel.ro/suporti-auto-tablete/',
                  'http://www.cel.ro/telefoane-mobile/',
                  'http://www.cel.ro/gadget_uri/',
                  'http://www.cel.ro/accesorii-gadget_uri/',
                  'http://www.cel.ro/accesorii-telefoane-mobile/',
                  'http://www.cel.ro/accesorii-diverse-telefoane/',
                  'http://www.cel.ro/acumulatori/',
                  'http://www.cel.ro/cabluri-telefoane-mobile/',
                  'http://www.cel.ro/car-kit_uri/',
                  'http://www.cel.ro/casti-bluetooth/',
                  'http://www.cel.ro/casti-telefoane-mobile/',
                  'http://www.cel.ro/folii-protectie/',
                  'http://www.cel.ro/huse-telefoane/',
                  'http://www.cel.ro/incarcatoare-telefoane/',
                  'http://www.cel.ro/incarcatoare-auto/',
                  'http://www.cel.ro/boxe-portabile/',
                  'http://www.cel.ro/baterii-externe/',
                  'http://www.cel.ro/ebook-reader/',
                  'http://www.cel.ro/accesorii-pda/',
                  'http://www.cel.ro/mp3-player/',
                  'http://www.cel.ro/accesorii-mp3-player/',
                  'http://www.cel.ro/reportofoane/',
                  'http://www.cel.ro/accesorii-reportofoane/',
                  'http://www.cel.ro/televizoare-lcd-led/',
                  'http://www.cel.ro/accesorii-televizoare/',
                  'http://www.cel.ro/suporturi-tv/',
                  'http://www.cel.ro/cabluri-tv/',
                  'http://www.cel.ro/ochelari-3d/',
                  'http://www.cel.ro/telecomenzi/',
                  'http://www.cel.ro/adaptoare-tv/',
                  'http://www.cel.ro/antene-externe/',
                  'http://www.cel.ro/kituri-de-curatare/',
                  'http://www.cel.ro/accesorii-diverse-pentru-tv_uri/',
                  'http://www.cel.ro/tv-box/',
                  'http://www.cel.ro/video-proiectoare/',
                  'http://www.cel.ro/accesorii-videoproiectoare/',
                  'http://www.cel.ro/ecrane-proiectie/',
                  'http://www.cel.ro/table-si-ecrane-interactive/',
                  'http://www.cel.ro/home-audio/',
                  'http://www.cel.ro/sisteme-home-cinema/',
                  'http://www.cel.ro/docking/',
                  'http://www.cel.ro/sisteme-audio/',
                  'http://www.cel.ro/dvd-playere-si-recordere/',
                  'http://www.cel.ro/bluray/',
                  'http://www.cel.ro/dvd-player/',
                  'http://www.cel.ro/dvd-portabil/',
                  'http://www.cel.ro/audio-hi-fi/',
                  'http://www.cel.ro/receivere/',
                  'http://www.cel.ro/boxe-podea/',
                  'http://www.cel.ro/procesoare/',
                  'http://www.cel.ro/placi-de-baza/',
                  'http://www.cel.ro/adaptoare-placi-de-baza/',
                  'http://www.cel.ro/placi-video/',
                  'http://www.cel.ro/adaptoare-placi-video/',
                  'http://www.cel.ro/monitoare-lcd-led/',
                  'http://www.cel.ro/monitoare-lcd-led-reconditionate/',
                  'http://www.cel.ro/hard-disk_uri/',
                  'http://www.cel.ro/hard-disk_uri-externe/',
                  'http://www.cel.ro/ssd_uri/',
                  'http://www.cel.ro/memorii/',
                  'http://www.cel.ro/carcase/',
                  'http://www.cel.ro/surse/',
                  'http://www.cel.ro/unitati-optice/',
                  'http://www.cel.ro/ventilatoare-carcasa/',
                  'http://www.cel.ro/accesorii-ventilatoare/',
                  'http://www.cel.ro/coolere-componente/',
                  'http://www.cel.ro/accesorii-coolere/',
                  'http://www.cel.ro/pasta-termoconductoare/',
                  'http://www.cel.ro/tv-tunere/',
                  'http://www.cel.ro/placi-de-sunet/',
                  'http://www.cel.ro/rack_uri/',
                  'http://www.cel.ro/accesorii/',
                  'http://www.cel.ro/boxe/',
                  'http://www.cel.ro/casti/',
                  'http://www.cel.ro/casti-gaming/',
                  'http://www.cel.ro/mouse/',
                  'http://www.cel.ro/mouse-pad/',
                  'http://www.cel.ro/mouse-gaming/',
                  'http://www.cel.ro/tastaturi/',
                  'http://www.cel.ro/tastaturi-gaming/',
                  'http://www.cel.ro/microfoane/',
                  'http://www.cel.ro/gaming/',
                  'http://www.cel.ro/jocuri/',
                  'http://www.cel.ro/console-jocuri/',
                  'http://www.cel.ro/gamepad-~-joystick/',
                  'http://www.cel.ro/scaune-gaming/',
                  'http://www.cel.ro/gaming-items/',
                  'http://www.cel.ro/medii-de-stocare/',
                  'http://www.cel.ro/usb-flash-drive/',
                  'http://www.cel.ro/carduri-memorie/',
                  'http://www.cel.ro/cititoare-de-carduri/',
                  'http://www.cel.ro/cd_uri-si-dvd_uri/',
                  'http://www.cel.ro/usb-hub/',
                  'http://www.cel.ro/ups/',
                  'http://www.cel.ro/accesorii-ups/',
                  'http://www.cel.ro/stabilizatori-tensiune/',
                  'http://www.cel.ro/prize/',
                  'http://www.cel.ro/acumulatori-ups/',
                  'http://www.cel.ro/camere-web/',
                  'http://www.cel.ro/conectica-/',
                  'http://www.cel.ro/cabluri-video/',
                  'http://www.cel.ro/cabluri-audio/',
                  'http://www.cel.ro/cabluri-periferice/',
                  'http://www.cel.ro/cabluri-componente/',
                  'http://www.cel.ro/adaptoare/',
                  'http://www.cel.ro/tablete-grafice/',
                  'http://www.cel.ro/accesorii-tablete-grafice/',
                  'http://www.cel.ro/calculatoare-desktop/',
                  'http://www.cel.ro/calculatoare-refurbished/',
                  'http://www.cel.ro/sisteme-server/',
                  'http://www.cel.ro/servere-configurabile/',
                  'http://www.cel.ro/servere-refurbished-reconditionate/',
                  'http://www.cel.ro/componente-server/',
                  'http://www.cel.ro/placi-de-baza-server/',
                  'http://www.cel.ro/hard-disk_uri-server/',
                  'http://www.cel.ro/controllere-raid/',
                  'http://www.cel.ro/procesoare-server/',
                  'http://www.cel.ro/memorii-server/',
                  'http://www.cel.ro/carcase-server/',
                  'http://www.cel.ro/placi-de-retea-server/',
                  'http://www.cel.ro/accesorii-server/',
                  'http://www.cel.ro/rack_uri-server/',
                  'http://www.cel.ro/multifunctionale/',
                  'http://www.cel.ro/consumabile/',
                  'http://www.cel.ro/cartuse-tonere-diverse/',
                  'http://www.cel.ro/accesorii-imprimante/',
                  'http://www.cel.ro/hartie/',
                  'http://www.cel.ro/imprimante-laser/',
                  'http://www.cel.ro/scannere/',
                  'http://www.cel.ro/faxuri/',
                  'http://www.cel.ro/imprimante-cu-jet/',
                  'http://www.cel.ro/plottere/',
                  'http://www.cel.ro/imprimante-foto/',
                  'http://www.cel.ro/imprimante-matriciale/',
                  'http://www.cel.ro/copiatoare/',
                  'http://www.cel.ro/consumabile-copiatoare/',
                  'http://www.cel.ro/accesorii-copiatoare/',
                  'http://www.cel.ro/birotica/',
                  'http://www.cel.ro/cititoare-coduri-de-bare/',
                  'http://www.cel.ro/masini-de-numarat-bani/',
                  'http://www.cel.ro/imprimante-termice/',
                  'http://www.cel.ro/distrugatoare-de-documente/',
                  'http://www.cel.ro/calculatoare-de-birou/',
                  'http://www.cel.ro/laminatoare/',
                  'http://www.cel.ro/centrale-telefonice/',
                  'http://www.cel.ro/centrale-telefonice-analogice/',
                  'http://www.cel.ro/telefoane/',
                  'http://www.cel.ro/centrale-telefonice-pbx-ip/',
                  'http://www.cel.ro/accesorii-centrale-telefonice/',
                  'http://www.cel.ro/sisteme-de-operare/',
                  'http://www.cel.ro/aplicatii-desktop/',
                  'http://www.cel.ro/antivirus/',
                  'http://www.cel.ro/editare-foto-video-audio/',
                  'http://www.cel.ro/wireless/',
                  'http://www.cel.ro/switch_uri/',
                  'http://www.cel.ro/switch_uri-kvm/',
                  'http://www.cel.ro/accesorii-kvm-/',
                  'http://www.cel.ro/routere/',
                  'http://www.cel.ro/network-attached-storage-nas/',
                  'http://www.cel.ro/placi-de-retea/',
                  'http://www.cel.ro/adaptor-retea/',
                  'http://www.cel.ro/printserver/',
                  'http://www.cel.ro/transceivere/',
                  'http://www.cel.ro/firewall/',
                  'http://www.cel.ro/cabluri-retea/',
                  'http://www.cel.ro/accesorii-retea/',
                  'http://www.cel.ro/camere-de-supraveghere/',
                  'http://www.cel.ro/accesorii-camere-supraveghere/',
                  'http://www.cel.ro/sisteme-dvr-~-nvr/',
                  'http://www.cel.ro/alarme/',
                  'http://www.cel.ro/accesorii-alarme/',
                  'http://www.cel.ro/videointerfoane/',
                  'http://www.cel.ro/aparate-foto-compacte/',
                  'http://www.cel.ro/accesorii-foto-compacte/',
                  'http://www.cel.ro/huse-_-genti/',
                  'http://www.cel.ro/aparate-foto-film/',
                  'http://www.cel.ro/aparate-foto-mirrorless/',
                  'http://www.cel.ro/aparate-foto-d_slr/',
                  'http://www.cel.ro/obiective-/',
                  'http://www.cel.ro/accesorii-aparate-foto/',
                  'http://www.cel.ro/acumulatori-baterii-incarcatoare/',
                  'http://www.cel.ro/genti/',
                  'http://www.cel.ro/trepiede-si-stative/',
                  'http://www.cel.ro/acumulatori-si-incarcatoare-dedicate/',
                  'http://www.cel.ro/blitz_uri-si-lumini/',
                  'http://www.cel.ro/accesorii-blitz_uri-si-lumini/',
                  'http://www.cel.ro/accesorii-obiective/',
                  'http://www.cel.ro/alte-accesorii/',
                  'http://www.cel.ro/protectie/',
                  'http://www.cel.ro/camere-video-digitale/',
                  'http://www.cel.ro/accesorii-camere-video/',
                  'http://www.cel.ro/echipamente-outdoor/',
                  'http://www.cel.ro/binocluri/',
                  'http://www.cel.ro/camere-video-outdoor/',
                  'http://www.cel.ro/rame-foto/',
                  'http://www.cel.ro/albume-foto/',
                  'http://www.cel.ro/climatizare/',
                  'http://www.cel.ro/aparate-de-aer-conditionat/',
                  'http://www.cel.ro/ventilatoare/',
                  'http://www.cel.ro/aparate-de-incalzire/',
                  'http://www.cel.ro/purificatoare-aer/',
                  'http://www.cel.ro/boilere/',
                  'http://www.cel.ro/frigidere-combine-frigorifice/',
                  'http://www.cel.ro/masini-de-spalat-rufe/',
                  'http://www.cel.ro/uscatoare-de-rufe/',
                  'http://www.cel.ro/masini-de-spalat-vase/',
                  'http://www.cel.ro/aragazuri/',
                  'http://www.cel.ro/hote/',
                  'http://www.cel.ro/incorporabile/',
                  'http://www.cel.ro/cuptoare-incorporabile/',
                  'http://www.cel.ro/masini-de-spalat-rufe-incorporabile/',
                  'http://www.cel.ro/masini-de-spalat-vase-incorporabile/',
                  'http://www.cel.ro/plite-incorporabile/',
                  'http://www.cel.ro/cantare-profesionale/',
                  'http://www.cel.ro/cuptoare-cu-microunde/',
                  'http://www.cel.ro/aparate-pentru-bucatarie/',
                  'http://www.cel.ro/roboti-de-bucatarie/',
                  'http://www.cel.ro/mixere/',
                  'http://www.cel.ro/masini-de-tocat/',
                  'http://www.cel.ro/cantare-de-bucatarie/',
                  'http://www.cel.ro/feliatoare-~-razatoare/',
                  'http://www.cel.ro/blendere-si-tocatoare/',
                  'http://www.cel.ro/aparate-de-vidat/',
                  'http://www.cel.ro/deshidratoare/',
                  'http://www.cel.ro/masini-pentru-paste-si-accesorii/',
                  'http://www.cel.ro/cani-filtrante-si-accesorii/',
                  'http://www.cel.ro/aparate-pentru-apa-si-cuburi-de-gheata/',
                  'http://www.cel.ro/preparat-paine/',
                  'http://www.cel.ro/masini-de-paine/',
                  'http://www.cel.ro/prajitoare/',
                  'http://www.cel.ro/sandwich-maker/',
                  'http://www.cel.ro/preparare-cafea/',
                  'http://www.cel.ro/espressoare/',
                  'http://www.cel.ro/cafetiere/',
                  'http://www.cel.ro/rasnite/',
                  'http://www.cel.ro/accesorii-espressoare/',
                  'http://www.cel.ro/capsule/',
                  'http://www.cel.ro/aparate-pentru-spuma-de-lapte/',
                  'http://www.cel.ro/aparate-de-gatit/',
                  'http://www.cel.ro/friteuze/',
                  'http://www.cel.ro/gratare-electrice/',
                  'http://www.cel.ro/aparate-de-gatit-cu-aburi/',
                  'http://www.cel.ro/aparate-preparat-desert/',
                  'http://www.cel.ro/aparate-speciale-de-gatit/',
                  'http://www.cel.ro/multicooker/',
                  'http://www.cel.ro/cuptoare-electrice/',
                  'http://www.cel.ro/plite/',
                  'http://www.cel.ro/aspiratoare/',
                  'http://www.cel.ro/accesorii-aspirator-~-curatenie/',
                  'http://www.cel.ro/preparare-bauturi/',
                  'http://www.cel.ro/storcatoare/',
                  'http://www.cel.ro/fierbatoare/',
                  'http://www.cel.ro/preparare-ceai/',
                  'http://www.cel.ro/preparare-sifon/',
                  'http://www.cel.ro/aparate-de-curatat-cu-aburi/',
                  'http://www.cel.ro/curatare-si-igienizare-cu-abur/',
                  'http://www.cel.ro/aspirare,-abur-si-filtrare-prin-apa/',
                  'http://www.cel.ro/mop-~-pistol-cu-aburi/',
                  'http://www.cel.ro/ingrijire-tesaturi/',
                  'http://www.cel.ro/fiare,-prese-si-statii-de-calcat/',
                  'http://www.cel.ro/masini-de-cusut/',
                  'http://www.cel.ro/masa-de-calcat-~-accesorii/',
                  'http://www.cel.ro/ingrijirea-parului/',
                  'http://www.cel.ro/placi-de-indreptat-parul/',
                  'http://www.cel.ro/ondulatoare-de-par/',
                  'http://www.cel.ro/uscatoare-de-par/',
                  'http://www.cel.ro/bigudiuri-/',
                  'http://www.cel.ro/aparate-de-coafat/',
                  'http://www.cel.ro/epilare,-tuns-si-barbierit/',
                  'http://www.cel.ro/epilatoare/',
                  'http://www.cel.ro/aparate-de-tuns/',
                  'http://www.cel.ro/aparate-de-ras/',
                  'http://www.cel.ro/accesorii-aparate-de-ras-si-epil/',
                  'http://www.cel.ro/aparate-de-tuns-parul-corporal/',
                  'http://www.cel.ro/trimmer-facial/',
                  'http://www.cel.ro/cosmetica-si-ingrijire/',
                  'http://www.cel.ro/aparate-manichiura-~-pedichiura/',
                  'http://www.cel.ro/aparate-ingrijire-ten/',
                  'http://www.cel.ro/oglinzi-cosmetice/',
                  'http://www.cel.ro/accesorii-aparate-ingrijire-ten/',
                  'http://www.cel.ro/ingrijire-dentara/',
                  'http://www.cel.ro/periute-electrice-si-irigatoare/',
                  'http://www.cel.ro/periute-manuale/',
                  'http://www.cel.ro/accesorii-ingrijire-dentara/',
                  'http://www.cel.ro/sanatate-si-intretinere/',
                  'http://www.cel.ro/cantare-personale/',
                  'http://www.cel.ro/tensiometre/',
                  'http://www.cel.ro/termometre-medicale/',
                  'http://www.cel.ro/glucometre/',
                  'http://www.cel.ro/fizioterapie/',
                  'http://www.cel.ro/fitness-si-aerobic/',
                  'http://www.cel.ro/biciclete-fitness/',
                  'http://www.cel.ro/benzi-de-alergat/',
                  'http://www.cel.ro/aparate-multifunctionale/',
                  'http://www.cel.ro/aparate-si-banci/',
                  'http://www.cel.ro/haltere-si-gantere/',
                  'http://www.cel.ro/saltele-si-covorase-fitness/',
                  'http://www.cel.ro/steppere-si-trambuline/',
                  'http://www.cel.ro/accesorii-fitness/',
                  'http://www.cel.ro/extensoare-si-benzi-elastice/',
                  'http://www.cel.ro/parfumuri-de-dama/',
                  'http://www.cel.ro/parfumuri-de-barbati/',
                  'http://www.cel.ro/parfumuri-unisex/',
                  'http://www.cel.ro/seturi-cadou/',
                  'http://www.cel.ro/deodorant/',
                  'http://www.cel.ro/produse-pentru-par/',
                  'http://www.cel.ro/masca/',
                  'http://www.cel.ro/sampon/',
                  'http://www.cel.ro/tratamente-de-par/',
                  'http://www.cel.ro/seturi-~-pachete-promo/',
                  'http://www.cel.ro/spuma,-fixativ,-gel/',
                  'http://www.cel.ro/serum,-defrizante,-spray/',
                  'http://www.cel.ro/crema,-ceara,-glossuri/',
                  'http://www.cel.ro/balsam/',
                  'http://www.cel.ro/vopsea-de-par/',
                  'http://www.cel.ro/perii-de-par/',
                  'http://www.cel.ro/produse-pentru-ten/',
                  'http://www.cel.ro/gel-de-ras-si-aftershave/',
                  'http://www.cel.ro/aparate-de-ras-clasice/',
                  'http://www.cel.ro/creme-si-demachiante/',
                  'http://www.cel.ro/masti,-exfoliant,-tonice/',
                  'http://www.cel.ro/tratamente,-serumuri/',
                  'http://www.cel.ro/creioane-corectoare/',
                  'http://www.cel.ro/protectie-solara-fata/',
                  'http://www.cel.ro/produse-pentru-corp/',
                  'http://www.cel.ro/igiena-intima/',
                  'http://www.cel.ro/gel-de-dus,-sapun-lichid/',
                  'http://www.cel.ro/lotiuni,-spray_uri,-creme/',
                  'http://www.cel.ro/creme-anti-celulita~antivergeturi/',
                  'http://www.cel.ro/creme-pentru-fermitate/',
                  'http://www.cel.ro/pachete-promotionale/',
                  'http://www.cel.ro/produse-soare/',
                  'http://www.cel.ro/accesorii-cosmetice/',
                  'http://www.cel.ro/make_up-~-unghii/',
                  'http://www.cel.ro/make_up-ochi/',
                  'http://www.cel.ro/make_up-buze/',
                  'http://www.cel.ro/make_up-ten/',
                  'http://www.cel.ro/manichiura/',
                  'http://www.cel.ro/accesorii-make_up/',
                  'http://www.cel.ro/accesorii-unghii/',
                  'http://www.cel.ro/ceasuri/',
                  'http://www.cel.ro/ceasuri-barbatesti/',
                  'http://www.cel.ro/ceasuri-de-dama/',
                  'http://www.cel.ro/ceasuri-unisex-~-copii/',
                  'http://www.cel.ro/ochelari-de-soare/',
                  'http://www.cel.ro/bijuterii/',
                  'http://www.cel.ro/bratari/',
                  'http://www.cel.ro/talismane/',
                  'http://www.cel.ro/pandantive/',
                  'http://www.cel.ro/clipsuri/',
                  'http://www.cel.ro/lanturi-pentru-bratari/',
                  'http://www.cel.ro/camera-copilului/',
                  'http://www.cel.ro/mobila-copii/',
                  'http://www.cel.ro/monitorizare-bebelusi-si-lampi-de-veghe-/',
                  'http://www.cel.ro/lenjerii-copii-si-accesorii-patut/',
                  'http://www.cel.ro/depozitare-jucarii/',
                  'http://www.cel.ro/mama-si-copilul/',
                  'http://www.cel.ro/carucioare-si-articole-de-transport/',
                  'http://www.cel.ro/igiena-si-ingrijire/',
                  'http://www.cel.ro/scutece-si-servetele/',
                  'http://www.cel.ro/alimentatie/',
                  'http://www.cel.ro/genti-scutece/',
                  'http://www.cel.ro/articole-mamici/',
                  'http://www.cel.ro/jucarii-si-jocuri/',
                  'http://www.cel.ro/jucarii-de-plus/',
                  'http://www.cel.ro/jucarii-bebelusi/',
                  'http://www.cel.ro/jucarii-muzicale/',
                  'http://www.cel.ro/jucarii-cu-telecomanda/',
                  'http://www.cel.ro/jucarii-de-exterior/',
                  'http://www.cel.ro/jucarii/',
                  'http://www.cel.ro/machete/',
                  'http://www.cel.ro/jucarii-interactive/',
                  'http://www.cel.ro/papusi-figurine-si-accesorii-papusi-/',
                  'http://www.cel.ro/vehicule-pentru-copii/',
                  'http://www.cel.ro/puzzle-si-lego/',
                  'http://www.cel.ro/gradinita-si-scoala/',
                  'http://www.cel.ro/ghiozdane-si-trolere/',
                  'http://www.cel.ro/rechizite/',
                  'http://www.cel.ro/costume-serbare/',
                  'http://www.cel.ro/generatoare-electrice/',
                  'http://www.cel.ro/insonorizate/',
                  'http://www.cel.ro/digitale_invertere/',
                  'http://www.cel.ro/uz-general/',
                  'http://www.cel.ro/turnuri-de-lumina/',
                  'http://www.cel.ro/automatizari/',
                  'http://www.cel.ro/aparate-de-sudura/',
                  'http://www.cel.ro/accesorii-sudura/',
                  'http://www.cel.ro/utilaje-de-constructii/',
                  'http://www.cel.ro/placi-compactoare/',
                  'http://www.cel.ro/finisoare-~-vibratoare-beton/',
                  'http://www.cel.ro/taietoare-materiale/',
                  'http://www.cel.ro/utilaje-agricole/',
                  'http://www.cel.ro/motosape/',
                  'http://www.cel.ro/motocultoare/',
                  'http://www.cel.ro/accesorii-utilaje-agricole/',
                  'http://www.cel.ro/articole-deszapezire/',
                  'http://www.cel.ro/pompe-si-motopompe/',
                  'http://www.cel.ro/accesorii-pompe-si-motopompe/',
                  'http://www.cel.ro/gradinarit/',
                  'http://www.cel.ro/scule-de-gradina/',
                  'http://www.cel.ro/masini-de-tuns-iarba/',
                  'http://www.cel.ro/decoratiuni-~-ingrasaminte/',
                  'http://www.cel.ro/scule-electrice-si-unelte/',
                  'http://www.cel.ro/masini-de-gaurit-si-insurubat/',
                  'http://www.cel.ro/scule-de-mana/',
                  'http://www.cel.ro/fierastraie/',
                  'http://www.cel.ro/polizoare/',
                  'http://www.cel.ro/ciocane-rotopercutoare/',
                  'http://www.cel.ro/suflante-cu-aer-cald/',
                  'http://www.cel.ro/masini-de-slefuit/',
                  'http://www.cel.ro/ciocane-demolatoare/',
                  'http://www.cel.ro/compresoare/',
                  'http://www.cel.ro/aparate-de-spalat-~-vopsit-cu-presiune/',
                  'http://www.cel.ro/motoare/',
                  'http://www.cel.ro/textile-pentru-casa/',
                  'http://www.cel.ro/perne/',
                  'http://www.cel.ro/lenjerii-de-pat/',
                  'http://www.cel.ro/cuverturi-~-paturi/',
                  'http://www.cel.ro/pilote/',
                  'http://www.cel.ro/prosoape/',
                  'http://www.cel.ro/halate-de-baie/',
                  'http://www.cel.ro/cearceafuri-si-fete-perna/',
                  'http://www.cel.ro/termometre-si-statii-meteo/',
                  'http://www.cel.ro/ceasuri-si-radio-cu-ceas/',
                  'http://www.cel.ro/becuri-si-corpuri-de-iluminat/',
                  'http://www.cel.ro/lanterne-si-accesorii/',
                  'http://www.cel.ro/becuri/',
                  'http://www.cel.ro/corpuri-de-iluminat/',
                  'http://www.cel.ro/sanitare/',
                  'http://www.cel.ro/chiuvete/',
                  'http://www.cel.ro/baterii-sanitare/',
                  'http://www.cel.ro/accesorii-sanitare/',
                  'http://www.cel.ro/siliconi-spume-si-solutii-tehnice/',
                  'http://www.cel.ro/combaterea-daunatorilor/',
                  'http://www.cel.ro/intretinere-casa-si-birou/',
                  'http://www.cel.ro/dispensere/',
                  'http://www.cel.ro/uscatoare/',
                  'http://www.cel.ro/dozatoare-sapun/',
                  'http://www.cel.ro/odorizante/',
                  'http://www.cel.ro/cosuri/',
                  'http://www.cel.ro/carucioare-curatenie/',
                  'http://www.cel.ro/curatenie-~-intretinere/',
                  'http://www.cel.ro/detergent-si-balsam-rufe/',
                  'http://www.cel.ro/curatenie-bucatarie/',
                  'http://www.cel.ro/hartie-igienica-si-accesorii-baie/',
                  'http://www.cel.ro/seifuri-lacate-feronerie/',
                  'http://www.cel.ro/bucatarie/',
                  'http://www.cel.ro/accesorii-bucatarie/',
                  'http://www.cel.ro/termometre-bucatarie/',
                  'http://www.cel.ro/filme/',
                  'http://www.cel.ro/filme-dvd/',
                  'http://www.cel.ro/filme-bluray/',
                  'http://www.cel.ro/filme-bluray-3d/',
                  'http://www.cel.ro/jocuri-de-societate/',
                  'http://www.cel.ro/accesorii-auto-exterioare-si-interioare/',
                  'http://www.cel.ro/cutii-portbagaj/',
                  'http://www.cel.ro/suport-auto-bicicleta/',
                  'http://www.cel.ro/huse/',
                  'http://www.cel.ro/anvelope-~-jante/',
                  'http://www.cel.ro/anvelope/',
                  'http://www.cel.ro/jante/',
                  'http://www.cel.ro/electrica-auto/',
                  'http://www.cel.ro/becuri-si-sigurante-auto/',
                  'http://www.cel.ro/baterii-auto/',
                  'http://www.cel.ro/statii-radio/',
                  'http://www.cel.ro/accesorii-statii-radio/',
                  'http://www.cel.ro/antene-statii-radio/',
                  'http://www.cel.ro/monitoare-auto/',
                  'http://www.cel.ro/navigatie-gps/',
                  'http://www.cel.ro/accesorii-navigatie-gps/',
                  'http://www.cel.ro/camere-video-auto/',
                  'http://www.cel.ro/detectoare-radar/',
                  'http://www.cel.ro/sisteme-audio-auto/',
                  'http://www.cel.ro/amplificatoare-auto/',
                  'http://www.cel.ro/boxe-auto/',
                  'http://www.cel.ro/player-auto/',
                  'http://www.cel.ro/subwoofer-auto/',
                  'http://www.cel.ro/lazi-frigorifice-auto/',
                  'http://www.cel.ro/intretinere-si-cosmetica-auto/',
                  'http://www.cel.ro/ulei-motor/',
                  'http://www.cel.ro/aditivi-auto/',
                  'http://www.cel.ro/stergatoare-auto/',
                  'http://www.cel.ro/pachete-revizie/',
                  'http://www.cel.ro/reparatii-si-echipamente-auto/',
                  'http://www.cel.ro/compresoare-redresoare-~-accesorii/',
                  'http://www.cel.ro/kit_uri-siguranta-auto/',
                  'http://www.cel.ro/scule-auto-~-accesorii/',
                  'http://www.cel.ro/vehicule-electrice/'
                  ]
    buy_tutton_path = '//*[@id="bodycode"]//form/button/text()'

    def request(self, url, callback):
        """
         wrapper for scrapy.request
        """
        request = scrapy.Request(url=url, callback=callback)
        request.cookies['cel_id'] = 'lpmagqv0j5108h2skpg73jpgb5'
        request.headers['User-Agent'] = (
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
            'like Gecko) Chrome/45.0.2454.85 Safari/537.36')
        return request

    def parse(self, response):
        meta = {'dont_redirect': True, 'handle_httpstatus_list': [302]}
        for href in response.xpath('//a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_page_contents, meta=meta)

    def parse_page_contents(self, response):
        url = response.url
        title = get_clean_string(response.xpath('//title/text()').extract())
        buy_button = get_clean_string(response.xpath(self.buy_tutton_path).extract())
        head = get_clean_string(response.xpath('/html/head').extract())
        body = get_clean_string(response.xpath('/html/body//*[not(self::script)]').extract())
        last_updated = datetime.utcnow()

        item = WebPageItem(url=url, title=title, buy_button=buy_button, last_updated=last_updated, head=head, body=body)

        return item
