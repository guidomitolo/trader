import React from 'react';
import { Outlet, Link } from "react-router-dom";


const Home = function () {
	return (
		<>
			<div className='m-10'>
				<h1 className="text-red-500">Coin Market App</h1>
				<nav class="navbar navbar-expand-lg bg-body-tertiary">
					<div class="container-fluid">
						<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
							<span class="navbar-toggler-icon"></span>
						</button>
						<div class="collapse navbar-collapse" id="navbarNav">
						<ul class="navbar-nav">
							<li class="nav-item">
								<Link class="nav-link" to={`/`}>Home</Link>
							</li>
							<li class="nav-item">
								<Link class="nav-link" to={`/table`}>Table</Link>
							</li>
							<li class="nav-item">
							<Link class="nav-link" to={`/charts`}>Charts</Link>
							</li>
						</ul>
						</div>
					</div>
				</nav>
			</div>
			<div>
				<Outlet />
			</div>
		</>
	);
};

export default Home