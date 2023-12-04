import styled from "styled-components"
import { FaPlus } from 'react-icons/fa';

export const ButtonPrimary = styled.button`
  /* Estilos padrão do botão */
  padding: 8px 14px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;

	display: flex;
	align-items:center;
	justify-content: center;

  /* Efeitos de hover */
  &:hover {
    background-color: #0056b3;
  }

  /* Efeitos de foco */
  &:focus {
    outline: none;
  }



`;

export const IconPlus = styled(FaPlus)`
  margin-right: 5px; /* Espaçamento entre o ícone e o texto */
`;
