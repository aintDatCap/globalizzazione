<script>
	import Navbar from '$lib/navbar.svelte';
	import globalizationImg from '$lib/assets/globalization.png';
</script>

<Navbar />

<article>
	<h2 class="title">Cos'è la globalizzazione?</h2>
	<p class="description">
		il termine globalizzazione è stato adoperato dagli anni 80 in poi per indicare un ampio insieme
		di fenomeni che hanno portato ad un avvicinamento delle culture. Ma la sua origine è più antica
		e alcuni studiosi pensano che derivi da un ossimoro utilizzato negli anni ‘60 dal sociologo
		canadese McLuhan. E’ interessante notare come McLuhan tragga ispirazione dall’esperienza della
		guerra in Vietnam, svoltasi proprio in quegli anni, vissuta da tutto il mondo simultaneamente,
		non solo in termini fisici, a causa delle numerose vittime di guerra, ma anche virtuali, in
		ragione dell’uso di mass media, come la televisione. “Postliterate man’s electronic media
		contract the world to a village or tribe where everything happens to everyone at the same time:
		everyone knows about and therefore participates in everything is happening the minute it
		happens. Television gives this quality of simultaneity to events in the global village.” “I
		media elettronici dell'uomo post alfabetizzato contraggono il mondo a un villaggio o tribù dove
		tutto accade a tutti allo stesso tempo: tutti conoscono e quindi partecipano a tutto ciò che sta
		accadendo di minuto in minuto. La televisione conferisce questa qualità di simultaneità agli
		eventi nel villaggio globale.” Altri studiosi invece limitano la definizione di globalizzazione
		a un processo puramente economico che ha come risultato a creazione di un mercato globale. A
		questo punto per dare una definizione unica alla globalizzazione possiamo citare il sociologo
		americano George Ritzer che parlando di questo fenomeno ha detto : “[…] la globalizzazione […]
		copre un'ampia gamma di fenomeni molto diversi. Per affrontare parte di questa complessità,
		abbiamo bisogno di una definizione di base di 'globalizzazione' come diffusione mondiale delle
		pratiche, espansione delle relazioni attraverso i continenti, organizzazione della vita sociale
		su scala globale e crescita di una coscienza globale condivisa.”

		<img src={globalizationImg} alt="Globalization" height="200px" width="200px" />
	</p>
</article>

<style>
	.description {
		margin-left: 3em;
		text-align: justify;
		margin-right: 3em;
	}

	.title {
		margin-left: 1em;
	}
</style>
