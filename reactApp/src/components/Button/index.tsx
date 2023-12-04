import { ButtonPrimary, IconPlus } from "./styles"



interface ButtonProps{
	title: string,

}

export function Button(props: ButtonProps) {
	return (
		<ButtonPrimary>
			<IconPlus/>
			{props.title}
			</ButtonPrimary>

	)
}
