<script lang="ts">
	import Navbar from '$lib/navbar.svelte';
	import Linechart from '$lib/Linechart.svelte';
	import data from '$lib/data/glob_data.json';
	import { Button } from 'sveltestrap';
	import footerStyle from '$lib/assets/footer_style.svg';
	let xRange: number[] = [];
	let yRange: number[] = [];
	for (let i = 1900; i <= 2015; i++) xRange.push(i);
	for (let i = 0; i <= 110; i += 10) yRange.push(i);

	const glob_data = JSON.parse(JSON.stringify(data));
</script>

<Navbar />

<article>
	<h2 class="title">Economia</h2>
	<p class="description">
		Citando il professor Luciano Gallino possiamo definire la globalizzazione economica come: “Il
		processo di costruzione di un mercato a livello planetario”. Il mercato globale ha avuto un
		grosso impulso dalle NICT (New Information and Communication Technologies) che hanno
		completamente eliminato le distanze fisiche trasformando il mercato globale in un cyber-mercato
		creando così anche la possibilità di trasformare dati, in merci e capitali dando così il via
		all’era dove tutto è a portata di un click. La globalizzazione a livello economico ha portato
		diversi benefici alla maggior parte degli Stati come ad esempio un arricchimento generale e la
		possibilità di avere tutti i prodotti in ogni periodo dell’anno.
	</p>

	<ul>
		<li>l’aumento delle disuguaglianze all’interno del sistema di stratificazione sociale</li>
		<li>l’aumento della disoccupazione e la riduzione dei salari reali</li>
		<li>
			la scomparsa di una reale concorrenza di fronte al monopolio delle grandi multinazionali
		</li>
		<li>
			il degrado economico, e talvolta l’annichilimento fisico di intere comunità, costrette alla
			dipendenza da forze economiche esterne e a un permanente sottosviluppo.
		</li>
	</ul>
	<p class="description">
		Questi aspetti negativi della globalizzazione si possono risolvere andando a limitare i poteri
		delle grandi multinazionali, ad esempio attraverso delle sanzioni alle aziende che decidono di
		delocalizzare oppure dare incentivi alle aziende del territorio che decidono di aprire nuove
		filiali all’interno dei confini del proprio Stato. In questo modo si potrebbe limitare il loro
		potere nei paesi meno sviluppati e proteggere anche industrie artigianali locali che non possono
		competere con le grandi industrie.
	</p>

	<div id="gdp_chart">
		<Linechart
			yText="PIL mondiale in bilioni di dollari US"
			xText="Crescita del PIL mondiale negli anni"
			{xRange}
			{yRange}
			data={glob_data}
			height={500}
			width={600}
			minX={1887}
		/>
	</div>
</article>
<img id="bkg_img" src={footerStyle} alt="" width="600" height="600" />

<footer>
	<Button href="/report/what-is-globalization" class="arrow" color="primary" outline>
		&#8592; Cos'è la globalizzazione
	</Button>
	<Button href="/report/culture" class="arrow" color="primary" outline>Cultura &#8594;</Button>
</footer>

<style>
	.description {
		margin-left: 3em;
		text-align: justify;
		margin-right: 3em;
	}

	.title {
		margin-left: 1em;
	}
	footer {
		text-align: center;
		position: fixed;
		bottom: 0;
		width: 100%;
		height: 10%;
	}
	#bkg_img {
		width: 100%;
	}
	#gdp_chart {
		text-align: center;
	}
	ul {
		margin-left: 4em;
	}
</style>
