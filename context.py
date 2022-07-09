context = {
    # スコアボードに表示する名前 (ハンドルネーム, チーム名 など)
    "display_name": "anonymous",
    # インスタンスに SSH 接続する際に使用するキーペア名
    # ※ あらかじめ東京リージョンにキーペアを登録しておく
    "key_name": "ekusiadadus-isucon-2022.pem",
    # インスタンスへの SSH 接続を許可するアクセス元の CDIR ブロック
    # ※ "{自身のグローバルIPv4アドレス}/32" を指定すればよい
    "allowed_cidr": "0.0.0.0/0",
    # スコアボードにスコアを送信するために必要な AWS 資格情報
    # ※ イベント当日に参加者に共有される
    "score_board_aws_access_key_id": "...",
    "score_board_aws_secret_access_key": "...",
}
