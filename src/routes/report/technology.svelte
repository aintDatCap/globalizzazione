<script lang="ts">
	import Navbar from '$lib/navbar.svelte';
	import { Button } from 'sveltestrap';
	import footerStyle from '$lib/assets/footer_style.svg';
	import immigrationGraph from '$lib/assets/graphs/USA_immigrants.png';
	import investmentsGraph from '$lib/assets/graphs/gdp_investments_graph.png';
	import exportsGraph from '$lib/assets/graphs/exports_gdp_graph.png';

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

	#imm_chart {
		margin: auto;
		display: block;
	}
</style>

<Navbar />
<article>
	<h2 class="title">Tecnologia</h2>
	<p class="description">
		Possiamo identificare il susseguirsi di tre fasi di globalizzazione dal punto di vista
		tecnologico. La prima coincidente con la fine del XIX° secolo, la seconda con gli anni dal 1945
		al 1980 e la terza con la fine del XX° secolo. La prima in particolare ci fa capire quanto la
		tecnologia influisca su questo fenomeno. Infatti intorno al 1870 si verificarono una serie di
		innovazioni tecnologiche cruciali per la diffusione internazionale del processo di
		industrializzazione: la costruzione di navi più robuste e veloci, con lo scafo in ferro, ridusse
		enormemente i tempi di navigazione; l’apertura del canale di Suez, nel 1869, dimezzò la durata
		del viaggio da Londra a Bombay; ma soprattutto l’inaugurazione del servizio telegrafico
		transatlantico permise alle comunicazioni transcontinentali di passare dalle settimane ai
		minuti. La riduzione dei tempi di percorrenza e dei costi, sia del trasporto su rotaia che di
		quello transoceanico, che della trasmissione delle informazioni via telegrafo, determinò quella
		accelerazione nei flussi commerciali internazionali, nei movimenti di capitale.
	</p>

	<img src={exportsGraph} alt="" />
	<img src={investmentsGraph} alt="" />
</article>
<img id="imm_chart" src={immigrationGraph} alt="" />
<img id="bkg_img" src={footerStyle} alt="" width="600" height="600" />
<footer>
	<Button href="/report/migration" color="primary" outline>&#8592; Migrazione</Button>
	<Button href="/report/enviroment" color="primary" outline>Ambiente &#8594;</Button>
</footer>
