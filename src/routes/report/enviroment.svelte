<script>
	import Navbar from '$lib/navbar.svelte';
	import { Button } from 'sveltestrap';
	import footerStyle from '$lib/assets/footer_style.svg';
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
</style>

<Navbar />
<article>
	<h2 class="title">Ambiente</h2>
	<p class="description">
		Riguardo al rapporto tra globalizzazione e ambiente non ci sono molti studi. A questa lacuna
		pone un parziale ma significativo rimedio un complesso studio realizzato da Jungho Baek e
		Yongsung Cho, dell'università del North Dakota (Stati Uniti d'America), insieme a Won W. Koo,
		dell'Università di Seul (Corea del Sud), i cui risultati sono stati resi noti in un recente
		articolo, The environmental consequences of globalization. Baek, Cho e Koo hanno preso in esame
		gli ultimi 50 anni di emissioni di anidride solforosa, in una serie di 50 diversi paesi, sia a
		economia avanzata sia a economia emergente o in via di sviluppo. I tre studiosi hanno quindi
		cercato di correlare, con opportuni modelli matematici, l'andamento storico delle emissioni
		inquinanti nei vari paesi sia con l'aumento della ricchezza (misurata in termini di PIL) sia con
		il grado di apertura dei mercati (misurato anche come incremento del commercio internazionale).
		La correlazione fra le tre variabili è risultata significativa solo in un numero limitato 17 di
		paesi. Questi, in sintesi, i risultati. Nei paesi a economia avanzata sia l'aumento della
		ricchezza sia l'apertura dei mercati ha determinato, in genere, un miglioramento della qualità
		ambientale.
	</p>
</article>
<img id="bkg_img" src={footerStyle} alt="" width="600" height="600" />
<footer>
	<Button href="/report/technology" color="primary" outline>&#8592; Tecnologia</Button>
	<Button href="/report/covid" color="primary" outline>Covid &#8594;</Button>
</footer>
