<script>
	import Navbar from '$lib/navbar.svelte';
	import {Button} from "sveltestrap"
</script>

<style>
	.description {
		margin-left: 3em;
		text-align: justify;
		margin-right: 3em;
	}

	.title {
		margin-left: 1em;
	}
	div {
		text-align: center;
	}
</style>

<Navbar />
<article>
	<h2 class="title">Cultura</h2>
	<p class="description">
		Ovviamente la globalizzazione ha portato alcune modifiche a livello socio culturale, infatti
		l’assenza del limite spazio-temporale ha causato, unitamente alla velocità, una maggiore
		diffusione di informazioni, di immagini, che a loro volta hanno comportato una
		universalizzazione di consumi, desideri, stili di vita, simboli e pratiche culturali. Non tutti
		gli Stati beneficiano in ugual misura della globalizzazione, è evidente che chi ne beneficia in
		misura maggiore è soprattutto il mondo occidentale, inteso come America del Nord, Europa, le
		grandi isole dell’Oceania, quindi popolazioni direttamente collegate a storia e mentalità di
		matrice europea. L’americanizzazione ( modo in cui alcuni studiosi chiamano questo aspetto della
		globalizzazione) si manifesta in tantissimi modi. Alcuni esempi di americanizzazione sono: i
		fast-food, i centri commerciali, i casinò stile Las Vegas, i film di hollywood. Modelli
		esportati nel resto del mondo con il risultato che gli individui di vari Paesi consumano gli
		stessi prodotti in scenari che somigliano molto, se non spudoratamente ricalcano, l’originale
		statunitense. Ciò che rende particolarmente grave questo fenomeno è che intere popolazioni
		stiano dimenticando o rifiutando la loro cultura per omologarsi ad uno stile di vita che
		soprattutto noi Europei e gli Stati Uniti predichiamo esportiamo all’estero, grazie ai mass
		media. Purtroppo non esiste un modo per risolvere completamente questo problema, l’unico modo
		per preservare la cultura di ogni nazione è quello di insegnarla ai più giovani, che senza
		demonizzare ciò che arriva dall’estero devono integrarla, senza annullare la propria identità.
	</p>
</article>
<div>
	<Button href="/report/economy"  color="primary" outline>&#8592; Economia</Button>
	<Button href="/report/migration"  color="primary" outline>Migrazione &#8594;</Button>
</div>