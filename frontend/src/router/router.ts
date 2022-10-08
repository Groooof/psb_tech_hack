import { createBrowserRouter } from 'react-router-dom';
import { ERoutes, RoutesComponents } from 'router/routes';

const router = createBrowserRouter([
	{
		path: ERoutes.Home,
		element: RoutesComponents[ERoutes.Home],
	},
]);

export { router };

// interface IEdited {
//     date: Date;
//     amount: number;
//     method: 'added' | 'removed';
// }

// interface IFoodItem {
//     id: string;
//     name: string;
//     createdAt: Date;
//     updatedAt: Date;
//     amountLasts: number;
//     edited?: Array<IEdited>
// }
