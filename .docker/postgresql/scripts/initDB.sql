create table users(
    user_id UUID NOT NULL,
    name VARCHAR(64) NOT NULL,
    mail VARCHAR(128),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
) ;

-- 行が更新された時に、updated_atに現在時刻を設定します。
CREATE FUNCTION set_updated_at() RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        NEW.updated_at := now();
        return NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- usersテーブル更新時に自動でupdated_atが更新されるようにトリガーを設定します。
CREATE TRIGGER trg_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE PROCEDURE set_updated_at();

INSERT INTO users(user_id, name, mail) VALUES ('806505cf-d8a5-bdd8-41f7-1fe7a7095ebf', 'nyosu', 'test_nyosu@test.com');
INSERT INTO users(user_id, name, mail) VALUES ('b91991d1-4cf6-b6d2-26e4-a48501c91bf4', 'motoy', 'test_motoyan@test.com');
UPDATE users SET name = 'motoyan' WHERE user_id = 'b91991d1-4cf6-b6d2-26e4-a48501c91bf4';