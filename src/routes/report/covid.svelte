<script>
	import Navbar from '$lib/navbar.svelte';
	import { Button } from 'sveltestrap';
	import ICTM_graph from '$lib/assets/graphs/ictm_graph.png';
	import footerStyle from '$lib/assets/footer_style.svg';
</script>

<Navbar />
<article>
	<h2 class="title">Covid</h2>
	<p class="description">
		Ormai da qualche anno tutto il mondo ha a che fare con la grave pandemia da Covid 19.
		Contrariamente a quello che si può pensare il processo di globalizzazione non ha subito arresti,
		anzi, grazie alle tecnologie attuali si è dato massimo spazio a un nuovo modo di lavorare: lo
		smart-working, tipologia di lavoro in essere da più di 20 anni ma poco utilizzata fino al 2020.
		Lo smart working è una nuova filosofia manageriale, fondata sulla restituzione alle persone di
		flessibilità e autonomia nella scelta degli spazi, degli orari e degli strumenti da utilizzare,
		a fronte di una maggiore responsabilizzazione sui risultati” Quindi si può riassumere in “work
		anytime, anywhere” Nel 2020, per effetto dell’impulso dato dal governo al ricorso dello smart
		working , a seguito dell’emergenza sanitaria, si è registrato una forte diffusione del lavoro da
		remoto: nel 2019, in Italia il numero stimato di lavoratori da remoto si attestava infatti a
		570.000, mentre nella primavera 2020 il numero dei lavoratori da remoto è lievitato a 6,58
		milioni. Lo smart working inoltre ha modificato l’idea stessa della ricerca del lavoro, infatti
		chi ha la possibilità di poter lavorare da casa non è costretto a cercare un lavoro nella zona
		in cui abita ma può addirittura decidere di cercare lavoro a livello internazionale, per cui si
		può parlare di una globalizzazione del lavoro: ad esempio esistono diversi siti che permettono
		ai giovani di cercare lavori e stage all’estero.
	</p>
</article>

<img src={ICTM_graph} alt="" />
<img id="bkg_img" src={footerStyle} alt="" width="600" height="600" />
<footer>
	<Button href="/report/enviroment" color="primary" outline>&#8592; Ambiente</Button>
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
</style>
