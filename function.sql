CREATE OR REPLACE FUNCTION Inserir_Aluno(p_nome VARCHAR, p_rga CHAR(14), p_curso_id INT)
RETURNS INT AS $$
DECLARE
    v_id INT;
BEGIN
    INSERT INTO tb_alunos (nome, rga, curso_id)
    VALUES (p_nome, p_rga, p_curso_id)
    RETURNING id INTO v_id;

    RETURN v_id;
END;
$$ LANGUAGE plpgsql;
