import React from 'react';
import { createBrowserRouter } from "react-router-dom";
import Home from './components/home/home.js';
import TablePage from './components/table/index.js';
import ChartsPage from './components/charts/index.js';
import ErrorPage from './error.js';


const routes = [
	{
		path: "/",
		element: <Home />,
		errorElement: <ErrorPage />,
		children: [
			{
				path: "table/",
				element: <TablePage/>,
			},
			{
				path: "charts/",
				element: <ChartsPage />,
			},
		]
	},
];


const router = createBrowserRouter(routes, {
	basename: "/",
});

export default router