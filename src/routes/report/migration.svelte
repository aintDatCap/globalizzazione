<script>
	import Navbar from '$lib/navbar.svelte';
	import { Button } from 'sveltestrap';
	import footerStyle from '$lib/assets/footer_style.svg';
</script>

<Navbar />
<article>
	<h2 class="title">Migrazione</h2>
	<p class="description">
		Il processo di globalizzazione ha determinato un’asimmetria tra politica ed economia con un
		notevole sbilanciamento a favore del secondo. Oggi il potere dello Stato non è messo in pericolo
		dall’invasione di uno Stato militarmente più forte, ma dalla mancanza di investimenti. I governi
		sono terrorizzati dalla fuga degli investitori che costituiscono il nucleo del potere economico
		globale e fanno di tutto affinché questi decidano di insediarsi nei loro territori. In questo
		modo il capitale, privo di qualunque tipologia di vincolo, gode della totale libertà di
		circolare alla ricerca di posti dove poter fare migliori investimenti. I governi, di qualunque
		connotazione politica, sono indotti a perdere sovranità e per incoraggiare l’arrivo delle
		imprese straniere, attivano le seguenti politiche neoliberiste:
	</p>
	<ul>
		<li>abbassamento delle tasse</li>
		<li>tagli alla spesa pubblica</li>
		<li>
			diminuzioni di vincoli ambientali e più in generale vengono favorite in tutto e per tutto le
			aziende investitrici.
		</li>
	</ul>
	<p class="description">
		I provvedimenti presi dai governi hanno diminuito il welfare e i diritti dei lavoratori e ciò ha
		determinato la radicalizzazione delle differenze salariali e la diminuzione del ceto medio.
		Secondo il sociologo Ulrich Beck dopo due secoli durante i quali l’Europa ha esportato
		manodopera, è diventata un’importante destinazione per i movimenti migratori: i nuovi poveri
		hanno cercato fortuna all’interno di altri Stati. Un modo per limitare questi effetti negativi
		della globalizzazione, potrebbe essere mandare agli stati meno sviluppati aiuti economici da
		investire in generale nel settore del lavoro, così da poter migliorare le condizioni di lavoro.
	</p>
</article>
<img id="bkg_img" src={footerStyle} alt="" width="600" height="600" />
<footer>
	<Button href="/report/economy" color="primary" outline>&#8592; Cultura</Button>
	<Button href="/report/technology" color="primary" outline>Tecnologia &#8594;</Button>
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
	ul {
		margin-left: 4em;
	}
</style>
