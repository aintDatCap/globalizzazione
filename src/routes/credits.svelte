<script>
	import Navbar from '$lib/navbar.svelte';
	import creditsStyle from '$lib/assets/credits_style.svg';
</script>

<style>
	h2 {
		margin-left: 0.3em;
	}

	div {
		background-image: url('$lib/assets/credits_style.svg');
		background-repeat: no-repeat;
		background-position: right bottom;
		padding-bottom: 50px;
	}
</style>

<Navbar />
<div>
	<h2>Creatori:</h2>
	<ul>
		<li>
			<p>Giovanni Sandri</p>
		</li>
		<li>
			<p>Federico Caprini</p>
		</li>
	</ul>

	<h2>Fonti:</h2>
	<ul>
		<li>
			<a
				href="https://drive.google.com/file/d/1Fvz82-K9SkcfrC2DTSeu5v2Q1lqTxAMK/view?usp=sharing"
				target="_blank">
				Definizione e Cultura
			</a>
		</li>
		<br />
		<li>
			<a
				href="https://drive.google.com/file/d/1BFVv0ukoSlAGBe8JRz-YQgDGOqp_pt0F/view?usp=sharing"
				target="_blank">
				Economia
			</a>
		</li>
		<br />
		<li>
			<a
				href="https://drive.google.com/file/d/1q8X5yNcsnMLY_D_n-hYT3KKjPQ_ow0VO/view?usp=sharing"
				target="_blank">
				Migrazione
			</a>
		</li>
		<br />
		<li>
			<a
				href="https://drive.google.com/file/d/1ocDXk7H-SJpQWdYmQXjckKEvhByqByO8/view?usp=sharing"
				target="_blank">
				Tecnologia
			</a>
		</li>
		<br />
		<li>
			<a
				href="https://www.scienzainrete.it/contenuto/articolo/Ambiente-e-globalizzazione"
				target="_blank">
				Ambiente
			</a>
		</li>
		<br />
		<li>
			<a href="https://morethesis.unimore.it/theses/available/etd-02202021-155630/" target="_blank">
				Covid
			</a>
			<a href="https://www.gazzettaufficiale.it/eli/id/1998/06/20/098G0229/sg" target="_blank">
				1
			</a>
			<a href="https://books.google.it/books?hl=it&lr=&id=9m1UDwAAQBAJ&oi=fnd&pg=PT4&dq=Smart+working,+job+crafting,+virtual+team,+empowerment,+Milano,+Wolters+Kluwer+Italia&ots=Y4mqvnKIQ3&sig=_GX9MmNtMhgmvppEDRr0amB5RYw#v=onepage&q=Smart%20working%2C%20job%20crafting%2C%20virtual%20team%2C%20empowerment%2C%20Milano%2C%20Wolters%20Kluwer%20Italia&f=false" target="_blank">
				2
			</a>
			<a href="https://www.eurofound.europa.eu/it/publications/report/2017/working-anytime-anywhere-the-effects-on-the-world-of-work" target="_blank">
				3
			</a>
			<a href="https://www.osservatori.net/it/ricerche/comunicati-stampa/cresce-il-numero-degli-smart-worker-italiani-570mila-plus20-lavoratori-piu-soddisfatti-degli-altri#:~:text=Nel%202019%20la%20percentuale%20di,farlo%20nei%20prossimi%20dodici%20mesi." target="_blank">
				4
			</a>
			<a href="http://www.comune.bologna.it/lavoro/servizi/119:6651/7708/" target="_blank">
				esempi
			</a>
		</li>
	</ul>
	<h2>Strumenti:</h2>
	<ul>
		<li>
			<p>Google scholar</p>
		</li>
		<li>
			<p>Sveltekit</p>
		</li>
		<li>
			<p>Sveltestrap</p>
		</li>
	</ul>

</div>
